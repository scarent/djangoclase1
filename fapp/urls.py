from django.contrib import admin
from django.urls import path 
from fapp import views as app1

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hola/",app1.display),
    path("ahora/",app1.displayDateTime),
    path("form/",app1.form),
]
