from django.conf.urls import url,include
from django.contrib import admin
# from  seat_app.views import home
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.init,name='init'),
    path('admin/', admin.site.urls),
    path("data/", views.send_data, name="send_data"),
    # path('index/', home.index),
    # path('stuindex/', home.stuindex),
    # path('login/', home.login),
    # path('register/', home.register),
    # path('userlist/', home.userlist),
    # url(r'^adduser/', home.adduser),
    # url(r'^edituser/(\d+)/', home.edituser),
    # url(r'^deluser/(\d+)/', home.deluser),
]