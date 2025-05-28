from django.urls import path

from .views import MenuItemListView, Generic

from .views import UserRegisterView, TokenObtainView
urlpatterns = [
    path('menu/', MenuItemListView.as_view(), name='menu-list'),
    path('menu/<int:id>/', Generic.as_view(), name='menu-detail'),
    path('signup/', UserRegisterView.as_view(), name='sign-up'),
    path('login/', TokenObtainView.as_view(), name='token-obtain'),
]




# This code defines the URL patterns for the menu app, allowing access to the list of menu items and individual menu item details.
# The first URL pattern maps to the `MenuItemListView`, which handles listing and creating menu items.
# The second URL pattern maps to the `Generic` view, which handles retrieving, updating, and deleting a specific menu item by its ID.
# This setup allows for a RESTful API interface for the menu items in the application.
# The `urlpatterns` list is used by Django to route incoming requests to the appropriate view based on the URL.
# The `name` parameter in each path allows for easy reference to these URLs in templates and other parts of the application.
# This code is part of a Django application that defines URL patterns for accessing menu items.
# The `MenuItemListView` handles listing all menu items and creating new ones.
# The `Generic` view allows for retrieving, updating, and deleting a specific menu item by its ID.
