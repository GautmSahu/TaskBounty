from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from AdminApp.models import App
from .forms import AppForm
from .common import ERROR_MESSAGE, handle_error_log, APP_NAME
from django.http import HttpResponse
import inspect


@login_required
def home(request):
    try:
        if request.user.is_authenticated:
            apps = App.objects.all()
            if request.user.is_superuser:
                return render(request, "admin/home.html", {"apps": apps, "user": request.user})
            else:
                return render(request, "user/home.html", {"apps": apps, "user": request.user})
        else:
            return redirect('/auth/login/')
    except Exception as e:
        handle_error_log(e,inspect.currentframe().f_code.co_name,APP_NAME)
        return HttpResponse(ERROR_MESSAGE)


@login_required
def app_create(request):
    try:
        if request.method == "POST":
            form = AppForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("home")
        else:
            form = AppForm()
        return render(request, "admin/app_form.html", {"form": form})
    except Exception as e:
        handle_error_log(e,inspect.currentframe().f_code.co_name,APP_NAME)
        return HttpResponse(ERROR_MESSAGE)


@login_required
def app_update(request, pk):
    try:
        app = get_object_or_404(App, pk=pk)
        if request.method == "POST":
            form = AppForm(request.POST, request.FILES, instance=app)
            if form.is_valid():
                form.save()
                return redirect("home")
        else:
            form = AppForm(instance=app)
        return render(request, "admin/app_form.html", {"form": form})
    except Exception as e:
        handle_error_log(e,inspect.currentframe().f_code.co_name,APP_NAME)
        return HttpResponse(ERROR_MESSAGE)


@login_required
def app_delete(request, pk):
    try:
        app = get_object_or_404(App, pk=pk)
        if request.method == "POST":
            app.delete()
            return redirect("home")
        return render(request, "admin/app_confirm_delete.html", {"app": app})
    except Exception as e:
        handle_error_log(e,inspect.currentframe().f_code.co_name,APP_NAME)
        return HttpResponse(ERROR_MESSAGE)