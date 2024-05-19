
from django.contrib import admin
from django.urls import include, path

from acceuil.views import index



urlpatterns = [
     path('', index, name='index'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('administrateur/', include('administrateur.urls')),
   
    # path('admin/', admin.site.urls),
]
