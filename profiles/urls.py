from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.test_view),
    url(r'^profile/$', views.profile, name='profile')
]
