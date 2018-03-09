from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home' ),
    url(r'^login/$', views.login_view, name='logout' ),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register_view, name='register'),
]
