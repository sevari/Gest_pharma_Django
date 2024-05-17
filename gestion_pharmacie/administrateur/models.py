from django.db import models

class Fourniseur(models.Model):
    NIF = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    def __str__(self):
        return self.nom
    
class Medicament(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)
    prix_achat = models.FloatField()
    prix_vente = models.FloatField()
    qte = models.IntegerField()
    fourniseur = models.ForeignKey(Fourniseur, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    
class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom
    
class Commande(models.Model):
    id_commande = models.AutoField(primary_key=True)
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_commande
    
class Ventecli(models.Model):
    id_vente = models.AutoField(primary_key=True)
    qte = models.IntegerField()
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    somme = models.FloatField()
    def __str__(self):
        return self.id_ligne_commande
 
class Livraison(models.Model):
    id_livraison = models.AutoField(primary_key=True)
    date = models.DateField()
    fourniseur = models.ForeignKey(Fourniseur, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_livraison
    
class Achat(models.Model):
    id_achat = models.AutoField(primary_key=True)
    qte = models.IntegerField()
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    livraison = models.ForeignKey(Livraison, on_delete=models.CASCADE)
    somme = models.FloatField()
    def __str__(self):
        return self.id_achat
    
class administrateur(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telephone = models.CharField(max_length=50)
    mdp = models.CharField(max_length=50)
    def __str__(self):
        return self.nom