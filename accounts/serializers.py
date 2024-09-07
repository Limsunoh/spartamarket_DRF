from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    def create(self, data):
        user = User.objects.create_user(
            email = data['email'],
            nickname = data['nickname'],
            name = data['name'],
            password = data['password'],
            birth_date = data['birth_date'],
            gender = data.get('gender', None),
            memo = data.get('memo', None),
            username = data['username']
            
        )
        return user
    class Meta:
        model = User
        fields = ['nickname', 'email', 'name', 'password',
                'birth_date', 'gender', 'memo', 'username']
        

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'nickname', 'email', 'name',
                'birth_date', 'gender', 'memo']
