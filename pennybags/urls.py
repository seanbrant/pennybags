from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login

from pennybags import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^collect/$', views.collect, name='collect'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
