from seat_app import  models
from django.forms import ModelForm
from django import  forms
from . import base
#校验输入的设备信息字段不能为空
class UserModelForm(base.BootstrapForm):
    class Meta:
        model = models.UserInfo
        fields = "__all__"
