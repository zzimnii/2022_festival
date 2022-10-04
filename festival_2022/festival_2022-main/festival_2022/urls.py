from django.contrib import admin
from django.urls import path, include
from postapp.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('postapp.urls')),
    #앱의 urls를 받아오는것
]

handler404 = page_not_found