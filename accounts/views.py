from django.shortcuts import get_object_or_404, render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .models import User
from .serializers import UserProfileSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class ProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer
    lookup_field = "username"
    

class Logout(APIView):
    def post(self, request):
        request.User.auth_token.delete()
        return Response(status=200)