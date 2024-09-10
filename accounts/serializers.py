from .models import User
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

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
        
        
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'nickname', 'email', 'name',
                'birth_date', 'gender', 'memo']
        
    def update(self, instance, validated_data):
        # 다른 사람의 아이디로 남의 프로필을 수정하려고 할때 권한 거부
        if self.context['request'].user != instance:
            raise PermissionDenied("프로필 수정할 권한이 없음.")
        return super().update(instance, validated_data)