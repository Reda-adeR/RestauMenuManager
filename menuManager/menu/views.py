# from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import MenuItem
from .serializers import MenuItemSerializer

# This one is for select all / and POST 
class MenuItemListView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# specific ID menu/ID
class MenuItemDetailView(RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'id'

# Update query with ID menu/ID
class MenuItemUpdateView(UpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'id'


#  DELETE query with ID menu/ID
class MenuItemDeleteView(DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'id'