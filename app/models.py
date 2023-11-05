from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class Custom_User_Model(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=8)
    last_name = models.CharField(max_length=10)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True)
    USERNAME_FIELD = "email"
    objects = UserManager()
    
    def __str__(self):
        return self.username
    
    def has_module_perms(self, app_label):
        return True
    
    def has_perm(self, obj=None):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin

