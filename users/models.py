from django.db import models
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone



from django.contrib.auth.models import AbstractUser,Group,Permission

# class CustomUser(AbstractUser):
#     # Your custom fields and methods
     
#     objects = CustomUserManager()
#     groups = models.ManyToManyField(
#         Group,
#         verbose_name=_('groups'),
#         blank=True,
#         help_text=_('The groups this user belongs to.'),
#         related_name='custom_users'  # Specify a unique related_name
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=_('user permissions'),
#         blank=True,
#         help_text=_('Specific permissions for this user.'),
#         related_name='custom_users'  # Specify a unique related_name
#     )


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractUser):
    # Your custom fields and methods
     
    objects = CustomUserManager()
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name='custom_users'  # Specify a unique related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_users'  # Specify a unique related_name
    )   

# Create your models here.
#class users_customuser(models.Models):
 
 #   pass
