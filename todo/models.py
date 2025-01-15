from django.db import models

class Task(models.Model):
    #タスク名を定義する
    title = models.CharField(max_length=200)
    #作成日を定義する
    created_at = models.DateTimeField(auto_now_add=True)
    #期限日を定義する
    due_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
