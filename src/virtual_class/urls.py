from django.conf.urls import include, url
from django.contrib import admin

from src.virtual_class import views


urlpatterns = [
    url(r'^first_page/user_logout/$', views.user_logout, name="user_logout"),
    url(r'^$', views.my_login, name="my_login"),
    url(r'^admin/', include(admin.site.urls))
]
