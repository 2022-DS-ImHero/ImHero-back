from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, name, is_mentor, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username = username,
            name = name,
            is_mentor = is_mentor
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, is_mentor,  password):
        user = self.create_user(
            email,
            password=password,
            username = username,
            name = name,
            is_mentor = is_mentor
        )
        # user.is_superuser = True
        user.is_admin = True
        # user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):

    mentor_choice = (('Y', 'Mentor'), ('N', 'Mentee'))
    email = models.EmailField(verbose_name='email', max_length=30, unique=True)
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    is_mentor = models.CharField(max_length=3, null=False, choices=mentor_choice)
    is_admin = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'is_mentor']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    def is_staff(self):
       return self.is_admin

