from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  

 
]

