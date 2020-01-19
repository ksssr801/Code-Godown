from django.conf.urls import url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import get_registered, get_logged_in, get_logged_out

router = DefaultRouter()
urlpatterns = router.urls
urlpatterns.append(url(r'register', get_registered, name='register'))
urlpatterns.append(url(r'login', get_logged_in, name='login'))
urlpatterns.append(url(r'logout', get_logged_out, name='logout'))
