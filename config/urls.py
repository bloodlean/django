from django.contrib import admin
from django.urls import path
from pages.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', index),
]
