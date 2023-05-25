from typing import Any
from django.db import models
from django.utils import timezone
# Create your models here.
class HashTag(models.Model):
    hashtag=models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag

class Blog(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField('date published')
    body=models.TextField()
    hashtag=models.ManyToManyField(HashTag)
    photo = models.ImageField(blank=True,null=True,upload_to="blog_photo")

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]
    
class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    comment_text = models.TextField()
    created_at = models.DateField(default=timezone.now)

    def apprve(self):
        self.save()

    def __str__(self):
        return self.comment_text
    
    
