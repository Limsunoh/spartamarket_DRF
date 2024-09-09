from . import views
from django.urls import path


app_name = "products"
urlpatterns = [
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:id>/', views.ProductDetailView.as_view(), name='product-detail'),
]