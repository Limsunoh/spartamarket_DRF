from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer, ProductCreateSerializer, ProductUpdateSerializer



        
class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer  # Create 시에는 생성용 시리얼라이저
        return ProductListSerializer  # List 시에는 목록용 시리얼라이저

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # author는 현재 사용자로 설정


# Retrieve, Update, and Delete a single product
class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ProductUpdateSerializer  # Update 시에는 업데이트용 시리얼라이저
        return ProductDetailSerializer  # Retrieve, Delete 시에는 상세용 시리얼라이저