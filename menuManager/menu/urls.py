from django.urls import path
from .views import MenuItemListView, MenuItemDetailView, MenuItemUpdateView, MenuItemDeleteView


urlpatterns = [
    path('menu/', MenuItemListView.as_view(), name='list-menu-items'),
    path('menu/<int:id>/', MenuItemDetailView.as_view(), name='menu-detail'),
    path('menu/<int:id>/', MenuItemUpdateView.as_view(), name='menu-update'),
    path('menu/<int:id>/', MenuItemDeleteView.as_view(), name='menu-delete')
]
