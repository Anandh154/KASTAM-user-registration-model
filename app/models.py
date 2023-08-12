from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.
class CustomManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('email is mandatory')
        ne=self.normalize_email(email)
        upo=self.model(email=ne,first_name=first_name,last_name=last_name)
        upo.set_password(password)
        upo.save()
        return upo
    def create_superuser(self,e,f_n,l_n,pw):
        upo=self.create_user(email=e,first_name=f_n,last_name=l_n,password=pw)
        upo.is_staff=True
        upo.is_superuser=True
        upo.save()
        


class CustomProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100,primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    objects=CustomManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']