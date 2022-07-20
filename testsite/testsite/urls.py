from django.contrib import admin
from django.urls import path, include # новое добавление
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')), # новое добавление
]