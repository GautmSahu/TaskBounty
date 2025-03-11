from django import forms
from AdminApp.models import App

class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ["name", "link", "category", "sub_category", "logo", "points"]
