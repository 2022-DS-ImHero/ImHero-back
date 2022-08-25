from django.contrib import admin
from .models import IdeaPost, Tag, CrewPost

# Register your models here.
admin.site.register(IdeaPost)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}


admin.site.register(Tag, TagAdmin)
admin.site.register(CrewPost)

