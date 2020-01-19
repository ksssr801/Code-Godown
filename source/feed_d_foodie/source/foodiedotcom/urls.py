from django.conf.urls import url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import get_restaurant_info, insert_data_func

router = DefaultRouter()
urlpatterns = router.urls
urlpatterns.append(url(r'restaurant-list', get_restaurant_info))
urlpatterns.append(url(r'insert-data-from-csv', insert_data_func))
