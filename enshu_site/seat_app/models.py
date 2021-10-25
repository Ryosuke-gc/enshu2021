from django.db import models

# Create your models here.

class UserInfo(models.Model):
    """
    用户信息表
    """
    username = models.CharField(verbose_name="username", max_length=32,unique=True)
    password = models.CharField(verbose_name="password", max_length=64)
    usertype = models.CharField(verbose_name='usertype', max_length=32)
    def __str__(self):
        return self.username
