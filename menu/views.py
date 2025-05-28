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