from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
# Create your views here.
from .models import MenuItem
from .serializers import MenuItemSerializer



class MenuItemListView(ListCreateAPIView):
    #  checker Token : soigjodfigj
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class Generic(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'id'


# # User registration view
# 
from rest_framework.response import Response
from .serializers import UserRegisterSerializer

class UserRegisterView(CreateAPIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User created successfully', 'user_id': user.id}, status=201)
        return Response(serializer.errors, status=400)