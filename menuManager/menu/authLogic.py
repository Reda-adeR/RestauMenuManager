
from .models import UserModel
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
    