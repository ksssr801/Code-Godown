from django.conf.urls import url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import write_blog#, park_the_vehicle, get_parking_lot_status, leave_the_parking_lot

router = DefaultRouter()
urlpatterns = router.urls
urlpatterns.append(url(r'write-your-blog', write_blog, name='write_blog'))
# urlpatterns.append(url(r'book-or-leave-parking-slot', park_the_vehicle))
# urlpatterns.append(url(r'leave-parking-slot', leave_the_parking_lot))
# urlpatterns.append(url(r'parking-lot-current-status', get_parking_lot_status))
