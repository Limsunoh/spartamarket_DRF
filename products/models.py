from django.db import models
from django.conf import settings


# # Create your models here.

# class TimeStampedModel(models.Model):
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# 	class Meta:
# 		abstract = True


# class Post(TimeStampedModel):
# 	author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# 	title = models.CharField(max_length=150)
# 	content = models.TextField()

# 	def __str__(self):
# 		return self.title

# 	class Meta:
# 		ordering = ["-title"]


# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, 
#                                 related_name="comments")
#     content = models.TextField()