from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url('admin/', admin.site.urls),
    url('myapi/', include('blogger_app.urls')),
    url('myapi/', include('accounts.urls')),
]
