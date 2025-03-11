from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from AdminApp.models import App
from UserApp.models import UserPoints
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from .common import ERROR_MESSAGE, handle_error_log, APP_NAME
from django.http import HttpResponse
import inspect


@login_required
def profile(request):
    try:
        return render(request, "user/profile.html", {"user": request.user})
    except Exception as e:
        handle_error_log(e,inspect.currentframe().f_code.co_name,APP_NAME)
        return HttpResponse(ERROR_MESSAGE)


@login_required
def earned_points(request):
    try:
        # Get all tasks taken by the user
        user_tasks = UserPoints.objects.filter(user=request.user)

        # Calculate total points
        total_points = user_tasks.aggregate(Sum("points"))["points__sum"] or 0
        return render(request, "user/earned_points.html", {"user_tasks": user_tasks, "total_points": total_points})
    except Exception as e:
        handle_error_log(e,inspect.currentframe().f_code.co_name,APP_NAME)
        return HttpResponse(ERROR_MESSAGE)


@login_required
def available_tasks(request):
    try:
        # Get all apps that the user has NOT taken
        taken_apps = UserPoints.objects.filter(user=request.user).values_list("app_id", flat=True)
        available_apps = App.objects.exclude(id__in=taken_apps)

        return render(request, "user/available_tasks.html", {"available_apps": available_apps})
    except Exception as e:
        handle_error_log(e,inspect.currentframe().f_code.co_name,APP_NAME)
        return HttpResponse(ERROR_MESSAGE)


@login_required
def take_task(request,app_id):
    try:
        app = get_object_or_404(App, id=app_id)

        if request.method == "POST" and request.FILES.get("screenshot"):
            screenshot = request.FILES["screenshot"]
            if screenshot:
                UserPoints.objects.create(user=request.user, app=app, screenshot=screenshot, points=app.points)
                return redirect("earned_points")  # Redirect to points earned page

        return render(request, "user/take_task.html", {"app": app})
    except Exception as e:
        handle_error_log(e,inspect.currentframe().f_code.co_name,APP_NAME)
        return HttpResponse(ERROR_MESSAGE)