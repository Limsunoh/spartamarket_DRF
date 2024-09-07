from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer, CommentSerializer, ArticleDetailSerializer
from django.shortcuts import get_object_or_404
from .models import Article, Comment
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated



class PostListAPIView(APIView):
    permission_classes=[
        IsAuthenticated
    ]

    def get(self, request):
        articles = Article.objects.all()  # Article 모델의 모든 데이터를 가져옴
        serializer = ArticleSerializer(articles, many=True)  # 여러 개의 데이터를 직렬화
        return Response(serializer.data)  # 직렬화된 데이터를 반환
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)  # 사용자로부터 받은 데이터를 직렬화
        # raise_exception=True로 설정하면, 유효하지 않은 데이터가 들어왔을 때 400 에러를 자동으로 반환함
        if serializer.is_valid(raise_exception=True):  # 데이터 유효성 검사
            serializer.save()  # 유효한 데이터일 경우 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # 생성된 데이터를 201 상태 코드와 함께 반환



class ArticleDetailAPIView(APIView):
    permission_classes=[
        IsAuthenticated
    ]
    def get_object(self, pk):
        # 주어진 pk 값에 해당하는 Article 객체를 반환. 객체가 없을 경우 404 에러를 반환.
        return get_object_or_404(Article, pk=pk)

    def get(self, request, pk):
        # 주어진 pk 값을 가진 Article 객체를 가져옴, 객체가 없을 경우 404 에러를 반환.
        article = self.get_object(pk)  
        # 가져온 Article 객체를 직렬화하여 JSON 형식으로 변환
        serializer = ArticleDetailSerializer(article)  
        # 직렬화된 데이터를 응답으로 반환
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        # 주어진 pk 값에 해당하는 Article 객체를 가져옴 (수정 대상),객체가 없을 경우 404 에러를 반환.
        article = self.get_object(pk)  
        # 기존의 article 객체를 클라이언트로부터 받은 새로운 데이터(request.data)로 갱신하기 위해 직렬화
        # partial=True는 일부 필드만 변경할 수 있도록 허용 (전체가 아닌 일부 필드만 수정 가능)
        serializer = ArticleDetailSerializer(article, data=request.data, partial=True)
        # 데이터가 유효한지 검사. 유효하지 않으면 400 Bad Request 응답을 자동으로 반환.
        if serializer.is_valid(raise_exception=True):  
            # 데이터가 유효할 경우 article 객체를 업데이트하여 저장
            serializer.save()  
            print(f"사용자로부터 받은 data를 기존 article로 change") 
            # 업데이트된 데이터를 응답으로 반환
            return Response(serializer.data) 
    
    def delete(self, request, pk):
        # 주어진 pk 값에 해당하는 Article 객체를 가져옴 (삭제 대상),객체가 없을 경우 404 에러를 반환.
        article = self.get_object(pk)  
        # 해당 article 객체를 삭제
        article.delete()  
        print(f"Article({pk}) is deleted.")
        # 삭제가 완료되었음을 나타내는 204 No Content 응답 반환
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class CommentListAPIView(APIView):

    permission_classes=[
        IsAuthenticated
    ]

    def get(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data) 
    
    def post(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            

class CommentDetailAPIView(APIView):
    permission_classes=[
        IsAuthenticated
    ]

    def get_object(self, comment_pk):
        return get_object_or_404(Comment, pk=comment_pk)
    
    
    def delete(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        comment.delete()
        data = {"pk": f"{comment_pk} is deleted."}
        return Response(data, status=status.HTTP_200_OK)
    
    
    def put(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)