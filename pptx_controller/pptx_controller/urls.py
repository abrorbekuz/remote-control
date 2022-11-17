from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    with open("index.html") as main:
        return HttpResponse( main.read() )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('key/', include('controls.urls')),
]
