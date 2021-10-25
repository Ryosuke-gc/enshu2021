from django.conf.urls import url,include
from django.contrib import admin
from  seat_app.views import home
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', home.index),
    url(r'^stuindex/', home.stuindex),
    url(r'^login/', home.login),
    url(r'^register/', home.register),
    url(r'^userlist/', home.userlist),
    # url(r'^adduser/', home.adduser),
    # url(r'^edituser/(\d+)/', home.edituser),
    # url(r'^deluser/(\d+)/', home.deluser),
]