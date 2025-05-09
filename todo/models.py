from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)  # blank=True 可以為空字串
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)  # null=True 為空物件
    important = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.title} - {self.created}"
