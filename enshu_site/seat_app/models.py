from django.db import models

# Create your models here.

class UserInfo(models.Model):
    """
    user information table
    """
    userid = models.CharField(verbose_name="userid", max_length=64,unique=True)
    username = models.CharField(verbose_name="username", max_length=64,unique=True)
    grade = models.CharField(verbose_name="grade", max_length=64)
    def __str__(self):
        return self.userid

class SeatInfo(models.Model):
    """
    seat information table
    """
    id = models.IntegerField(verbose_name="id", max_length=32,unique=True)
    seatid = models.IntegerField(verbose_name="seatid", max_length=32)
    status = models.IntegerField(verbose_name="status", max_length=32)
    time = models.TimeField(verbose_name="time")

    def __str__(self):
        return self.seatid

class User2Seat(models.Model):
    """
    user - seat information table
    """
