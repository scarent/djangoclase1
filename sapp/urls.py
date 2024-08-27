from django.contrib import admin
from django.urls import path, include
from sapp import views as app2

urlpatterns=[
    path('admin/', admin.site.urls),
    path("saludo/",app2.sapp),
]