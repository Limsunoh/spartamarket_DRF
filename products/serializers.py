from .models import Product
from rest_framework import serializers


class ProductListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ["title"]

# 제품 상세 조회에 사용되는 시리얼라이저
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "author", "title", "content", "image", "created_at", "updated_at"]  

# 제품 생성에 사용되는 시리얼라이저
class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "content", "image"]  

# 제품 업데이트에 사용되는 시리얼라이저
class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "content", "image"] 