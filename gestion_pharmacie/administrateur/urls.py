from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('commande_fournisseur/', views.commande_fournisseur, name="commande_fournisseur"),
]
