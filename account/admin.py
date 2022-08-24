from django.contrib import admin
from account.models import CustomUser
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForm, UserCreationForm
# Register your models here.

class AccountAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'username', 'name', 'is_mentor')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'is_mentor')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'name', 'is_mentor', 'password1', 'password2')}
         ),
    )
    search_fields = ('email','name')
    ordering = ('name',)
    filter_horizontal = ()

admin.site.register(CustomUser, AccountAdmin)
admin.site.unregister(Group)