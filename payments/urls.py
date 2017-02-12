from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add-funds/$', views.add_funds, name='add_funds'),
]
