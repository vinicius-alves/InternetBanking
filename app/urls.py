from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.authtoken import views as authviews
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()

#rest webservices
urlpatterns +=[
    url(r'^ws/login/$', authviews.obtain_auth_token, name='login'),
    url(r'^ws/logout/$', views.logout, name='logout'),
]
