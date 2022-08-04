from ssl import create_default_context
from django.db import models
from django.urls import reverse

class Post(models.Model):

    title = models.CharField(verbose_name='Title', max_length=100)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    image = models.ImageField(verbose_name='Picture', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Date of creation', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date of change', auto_now=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("index")

class Comment(models.Model):

    description = models.TextField(verbose_name='Description', null=True, blank=True)
    post = models.ForeignKey(Post, related_name='Сomments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Date of creation', auto_now_add=True)

    def __str__(self):
        return f'{self.description}'

    def get_absolute_url(self):
        return reverse("index")
    
    
class Message(models.Model):
    title = models.CharField(verbose_name='Subject', max_length=250, null=True, blank=True)
    body = models.TextField(verbose_name='Body')

    def __str__(self):
        return f'{self.body}'
