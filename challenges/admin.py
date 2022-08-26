from django.contrib import admin
from .models import ChallengeTag, Category, Post, Comment
# Register your models here.

class CategroyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}
admin.site.register(ChallengeTag)
admin.site.register(Category, CategroyAdmin)
admin.site.register(Post)
admin.site.register(Comment)

