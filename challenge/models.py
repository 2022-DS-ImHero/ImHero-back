from django.db import models

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



