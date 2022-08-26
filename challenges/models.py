from tkinter import CASCADE
from unicodedata import category
from django.db import models
from account.models import CustomUser
# Create your models here.

class ChallengeTag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/challenge/category/{self.slug}'

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='professor/my_image')
    date = models.DateField()

    tags = models.ManyToManyField(ChallengeTag, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/post/{self.pk}/'
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} :: {self.content}'
