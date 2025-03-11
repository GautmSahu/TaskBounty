from django.db import models
from django.contrib.auth.models import User
from AdminApp.models import App

class UserPoints(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    points = models.IntegerField()
    screenshot = models.ImageField(upload_to="screenshots/")

    def __str__(self):
        return f"{self.user.username} - {self.app.name}"
    
    class Meta:
        indexes = [
            models.Index(fields=['user', 'app', 'id']),  # Composite Index on user, app and id
        ]