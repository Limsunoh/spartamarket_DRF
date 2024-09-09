from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)


urlpatterns = [
    path('signup/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path("login/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("logout/", TokenBlacklistView.as_view(), name='logout'),
    path("<str:username>/", views.ProfileView.as_view(), name='profileview'),
]
#