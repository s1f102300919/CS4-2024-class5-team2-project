from django.db import models

class Task(models.Model):
    #タスク名を定義する
    title = models.CharField(max_length=200)
    #期限日を定義
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
    
