from django.db.migrations import serializer
from DRF_market.products.models import Post
from DRF_market.accounts.models import User


class AuthorSerializer(serializer.ModelSerializer):
	class Meta:
		model = User
		fields = ["id", "username", "email", "password"]


class PostListSerializer(serializer.ModelSerializer):
	class Meta:
		model = Post
		fields = ["id", "title"]
