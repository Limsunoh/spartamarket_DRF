from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer, ProductCreateSerializer, ProductUpdateSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly



        
class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer  # Create 시에는 생성용 시리얼라이저
        return ProductListSerializer  # List 시에는 목록용 시리얼라이저

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # author는 현재 사용자로 설정



# 제품 상세 검색, 업데이트 및 삭제
class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]

# PUT, DELETE로 들어오면 해당 serializer 실행 
    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ProductUpdateSerializer  # Update 시에는 업데이트용 시리얼라이저
        return ProductDetailSerializer  # Delete가 들어오면 시리얼라이즈랑 관계없이 삭제처리됨.