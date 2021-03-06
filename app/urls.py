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
    url(r'^ws/login/$',    authviews.obtain_auth_token, name='login'),
    url(r'^ws/logout/$',   views.logout,   name='logout'   ),
    url(r'^ws/balance/$',  views.balance,  name='balance'  ),
    url(r'^ws/excerpt/$',  views.excerpt,  name='excerpt'  ),
    url(r'^ws/withdraw/$', views.withdraw, name='withdraw' ),
    url(r'^ws/deposit/$',  views.deposit,  name='deposit'  ),
    url(r'^ws/transfer/$', views.transfer, name='transfer' ),
    url(r'^ws/help/$',     views.help,     name='help'     ),
]
