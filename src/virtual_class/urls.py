from django.conf.urls import include, url
from django.contrib import admin


from src.virtual_class import views


urlpatterns = [
    # url(r'^$/user_logout/$', views.user_logout, name="user_logout"),

    url(r'^$', views.my_login, name="my_login"),
    url(r'^staff/$', views.staff, name="staff"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^staff/logout/$', 'django.contrib.auth.views.logout',{'next_page':"my_login" }),
    url(r'^staff/all_students/$', views.all_students, name="all_students"),
]
