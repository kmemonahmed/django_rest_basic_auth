from rest_framework.views import APIView
from rest_framework.response import Response

from main.models import CustomUser

# Login Api
class LoginView(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            return Response({'message': 'Login Successfully', 'status': 200}, 200)
        else:
            return Response({'message': 'Login Failed', 'status': 400}, 400)

# Logout Api
class LogoutView(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            return Response({'message': 'Logout Successfully', 'status': 200}, 200)
        else:
            return Response({'message': 'Logout Failed', 'status': 400}, 400)
