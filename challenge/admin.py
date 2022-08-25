from ctypes.wintypes import tagMSG
from django.contrib import admin
from .models import Professor, Company, Senior, ChallengeTag, Comment, ReComment
# Register your models here.

admin.site.register(Professor)
admin.site.register(Comment)
admin.site.register(ReComment)

admin.site.register(Company)
admin.site.register(Senior)
admin.site.register(ChallengeTag)