from django.db import models
from account.models import CustomUser
# Create your models here.

class ChallengeTag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Professor(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='professor/my_image')
    date = models.DateField()

    tags = models.ManyToManyField(ChallengeTag, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Professor, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} :: {self.content}'

class ReComment(models.Model):
    post = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Company(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='company/my_image')
    date = models.DateField()

    tags = models.ManyToManyField(ChallengeTag, blank=True)

    def __str__(self):
        return self.title

class Senior(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='senior/my_image')
    date = models.DateField()

    tags = models.ManyToManyField(ChallengeTag, blank=True)
    
    def __str__(self):
        return self.title



