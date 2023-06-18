from rest_framework import serializers
from .models import User,Todo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = "__all__"

class TodoSerailizer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    #
    # def get_user(self, obj):
    #     return obj.user.name
    class Meta:
        model=Todo
        fields ="__all__"
