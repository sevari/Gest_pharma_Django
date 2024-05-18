
from django.contrib import admin
from django.urls import include, path

from acceuil.views import index
from administrateur.views import commande_fournisseur



urlpatterns = [
    path('', index, name='index'),
    path('commande_fournisseur', commande_fournisseur, name='commande_fournisseur'),
    path("__reload__/", include("django_browser_reload.urls")),
   
    # path('admin/', admin.site.urls),
]
