from django.shortcuts import render

from administrateur.models import Fourniseur



def dashboard(request):
    return render(request, 'dashboard.html')


def commande_fournisseur(request):
    fournisseurs = Fourniseur.objects.all()
    fournisseur_selectionne_details = None

    if request.method == 'POST':
        fournisseur_nif = request.POST.get('supplier')
        if fournisseur_nif:
            try:
                fournisseur_selectionne = Fourniseur.objects.get(NIF=fournisseur_nif)
                fournisseur_selectionne_details = {
                    'NIF': fournisseur_selectionne.NIF,
                    'Nom': fournisseur_selectionne.nom,
                    'Adresse': fournisseur_selectionne.adresse,
                    'Téléphone': fournisseur_selectionne.telephone,
                    'Email': fournisseur_selectionne.email
                }
            except Fourniseur.DoesNotExist:
                fournisseur_selectionne_details = None

    return render(request, "commande_fournisseur.html", {'fournisseurs': fournisseurs, 'fournisseur_selectionne_details': fournisseur_selectionne_details})


