from django.urls import path
from .views import profile, earned_points, available_tasks, take_task

urlpatterns = [
    path("profile/", profile, name="profile"),
    path("earned-points/", earned_points, name="earned_points"),
    path("available-tasks/", available_tasks, name="available_tasks"),
    path("take-task/<int:app_id>/", take_task, name="take_task"),
]
