from django.db import models

# Create your models here.
class Post(models.Model):
    subject = models.CharField(max_length=100)
    time = models.CharField(max_length=5)  # 時間を文字列として保存（例："1:20"）
    comment = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject