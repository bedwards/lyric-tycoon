from django.contrib import admin
from django.urls import path
from app.views import sentences

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sentences/', sentences, name='sentences'),
]
