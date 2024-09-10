from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from .models import User
from .serializers import UserProfileSerializer, UserSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.
class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class ProfileView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "username"
    
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return UserUpdateSerializer
        return UserProfileSerializer
    

