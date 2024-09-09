from django.db import models
from django.conf import settings



class TimeStampedModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Product(TimeStampedModel):
	author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	content = models.TextField()
	image = models.ImageField(default='default_image.jpeg', upload_to='uploads/', height_field=None, width_field=None, max_length=None)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-id"]


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, 
                                related_name="comments")
    content = models.TextField()
    
    def __str__(self):
        return self.content[:20]