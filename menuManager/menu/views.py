# from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import MenuItem, UserModel
from .serializers import MenuItemSerializer, UserModelSerializer

from rest_framework.response import Response
from django.contrib.auth.hashers import check_password


class BasicAuthChecker:
    def initial(self, request, *args, **kwargs):
        username = request.data.get('userName')
        password = request.data.get('pswd')

        if not username or not password: return self._unauthorized_response()

        try:
            user = UserModel.objects.get(userName=username)
        except UserModel.DoesNotExist:
            return self._unauthorized_response()

        if not check_password(password, user.pswd): return self._unauthorized_response()

        # If all good, call parent initial (continues processing)
        return super().initial(request, *args, **kwargs)

    def _unauthorized_response(self):
        from rest_framework.exceptions import PermissionDenied
        raise PermissionDenied(detail="Invalid username or password")
    

# This one is for select all / and POST 
class MenuItemListView(BasicAuthChecker, ListCreateAPIView):
    #  checker Token : soigjodfigj
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    


# specific ID menu/ID
class Generic(BasicAuthChecker, RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'id'



#  Login/Logout API's
class LoginUser(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer