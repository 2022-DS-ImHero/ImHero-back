from django.contrib import admin
from .models import IdeaPost, Tag, CrewPost

# Register your models here.
admin.site.register(IdeaPost)
admin.site.register(Tag)
admin.site.register(CrewPost)