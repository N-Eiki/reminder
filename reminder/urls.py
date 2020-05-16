from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("remind.urls")),
    url(r'^webpush/', include('webpush.urls')),
]
