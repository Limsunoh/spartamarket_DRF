from . import views
from django.urls import path


app_name = "products"
urlpatterns = [
    path("", views.ArticleListAPIView.as_view(), name="article_list"),
    path("<int:pk>/", views.ArticleDetailAPIView.as_view(), name="article_detail"),
    path("<int:article_pk>/comments/", 
        views.CommentListAPIView.as_view(),
        name="comment_list"),
    path("comments/<int:comment_pk>/",
        views.CommentDetailAPIView.as_view(),
        name="comment_delete"),
    
    
]