from django.db import models
from django.contrib.auth.models import AbstractUser , Group,Permission


class registermodel(AbstractUser):

    # username=models.CharField(max_length=100)
    # email = models.EmailField()
    dob = models.DateField(max_length=100)
    gender = models.CharField(max_length=100)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Set a unique related_name
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Set a unique related_name
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

