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
    
    
    # 강의 class 참고용
# class ProfileView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self, request, username):
#         user = get_object_or_404(User, username=username)
#         serializer = UserProfileSerializer(user)
#         return Response(serializer.data, status=200)
    
class ProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer
    lookup_field = "username"