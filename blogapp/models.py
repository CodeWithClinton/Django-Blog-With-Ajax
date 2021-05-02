from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to = 'img')
    title = models.CharField(max_length = 50)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'name')
    body = models.TextField()
    slug = models.SlugField()
    created_on = models.DateTimeField(auto_now= True)
    updated = models.DateTimeField(auto_now= True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length = 50)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= 'comments')
    def __str__(self):
        return self.body
