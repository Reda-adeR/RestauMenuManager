from django.urls import path
from .views import MenuItemListView, Generic, LoginUser, AccountLogin


urlpatterns = [
    path('menu/', MenuItemListView.as_view(), name='list-menu-items'),
    path('menu/<int:id>/', Generic.as_view(), name='menu-detail'),
    path('subs/', LoginUser.as_view(), name='Sign-up'),
    path('log/', AccountLogin.as_view(), name='Sign-in')
]
