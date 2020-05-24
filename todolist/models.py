from django.db import models

class Todolist(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    duedate=models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Todolist, on_delete=models.CASCADE, related_name='comments')
    content=models.TextField()

    def __str__(self):
        return self.post
# Create your models here.
