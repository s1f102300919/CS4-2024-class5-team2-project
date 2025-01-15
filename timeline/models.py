from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    subject = models.CharField(max_length=100)
    time = models.CharField(max_length=5)  # 時間を文字列として保存（例："1:20"）
    comment = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.subject
    
    def total_likes(self):
        """いいねの合計を返す"""
        return self.likes.count()