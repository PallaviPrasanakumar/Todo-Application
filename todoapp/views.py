from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import User,Todo
from .serializers import  UserSerializer,TodoSerailizer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# Create your views here.
def hello(request):
    return JsonResponse({
        "message" : "Hello welcome to todoapp"
    },status=200)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerailizer
#
# @api_view(http_method_names=["POST"])
# def create_user(request):
#     print(request.data)
#     return Response({
#         "message" : "Received"
#     })
