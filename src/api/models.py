from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ToDo(models.Model):
    name = models.CharField(verbose_name='todo_name', max_length=60)
    text = models.TextField(blank=True)
    author = models.ForeignKey(to=User, related_name='todos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ToDo/', blank=True)
    is_published = models.BooleanField(default=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = "todo's"

    def __str__(self):
        return f'{self.name} был создан:{self.upload_time}'

