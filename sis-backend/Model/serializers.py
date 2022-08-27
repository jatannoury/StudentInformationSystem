from rest_framework.serializers import ModelSerializer
from .models import sisUser

class UserSerializer(ModelSerializer):
    class Meta:
        model=sisUser
        fields="__all__"