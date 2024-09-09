from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name = "products"
urlpatterns = [
    path('', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:id>/', views.ProductDetailView.as_view(), name='product-detail'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)