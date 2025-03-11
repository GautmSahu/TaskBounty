from rest_framework import serializers
from AdminApp.models import App
from UserApp.models import UserPoints

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'


class UserPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPoints
        fields = '__all__'
