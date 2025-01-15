from django.db import models

class Note(models.Model):
    subject = models.CharField(max_length=100)
    notes = models.TextField()
    time_spent = models.CharField(max_length=8)  # 時間の形式を保存

    def __str__(self):
        return self.subject

