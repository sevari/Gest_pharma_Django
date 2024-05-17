from django.db import models

#Model fourniseur ahafahatsika mahafantatra oe inona daolo no ilaina mikasika ny fournisseur
class Fourniseur(models.Model):
    NIF = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    def __str__(self):
        return self.nom
    
    
#modele medicament ndray mitahiry ny information mikasika ny  fanafody reetra ao anaty pharmacie
class Medicament(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)
    prix_achat = models.FloatField()
    prix_vente = models.FloatField()
    qte = models.IntegerField()
    fourniseur = models.ForeignKey(Fourniseur, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
   
#modele client ahafahana maka information mikasika ny client, 
# natao realise kokoa ilay izy hoe anarana no max alaina am client am resaka facture 
class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom


#ito ndray tableau commande ahafahana manao commande ny client eto no miasa ilay systeme de panier
#zany oe ito no mitondra ny zavatra reetra comandenn'ny client  de regrouper ato daholo 
class Commande(models.Model):
    id_commande = models.AutoField(primary_key=True)
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_commande
    
#ito ndray table manao relation amin'ny medicament sy commande no sad koa element anankiray ao anaty commande
#zany oe possible mividy fanafody samihafa de le izy element commande ray de mividy fanafody samihafa de otran ito maro2 no mifandray am comande

class Ventecli(models.Model):
    id_vente = models.AutoField(primary_key=True)
    qte = models.IntegerField()
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    somme = models.FloatField()
    def __str__(self):
        return self.id_ligne_commande
 
 
#ito ndray table livraison ahafahana manao relation amin'ny fourniseur sy ny livraison anreo medicament ateriny
#miregouper maro2 koa ito zany oe achat fanafody maro2 no ato de amzay mora2 ny mijery livraison 
class Livraison(models.Model):
    id_livraison = models.AutoField(primary_key=True)
    date = models.DateField()
    fourniseur = models.ForeignKey(Fourniseur, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_livraison

# ireo fanafody zay nolivrena tao anty livraison iray, table maro2 otran ito no mifandray am livraison de lasa anankiray
class Achat(models.Model):
    id_achat = models.AutoField(primary_key=True)
    qte = models.IntegerField()
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    livraison = models.ForeignKey(Livraison, on_delete=models.CASCADE)
    somme = models.FloatField()
    def __str__(self):
        return self.id_achat
    
    
#ito ndray table administrateur ahafahana manao relation amin'ny utilisateur sy ny user
class administrateur(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telephone = models.CharField(max_length=50)
    mdp = models.CharField(max_length=50)
    def __str__(self):
        return self.nom