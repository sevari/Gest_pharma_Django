from django.db import models

#Model fourniseur ahafahatsika mahafantatra oe inona daolo no ilaina mikasika ny fournisseur
class Fourniseur(models.Model):
    NIF = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    def fournisseur(self):
        return {'NIF':self.NIF, 'nom':self.nom, 'adresse':self.adresse, 'telephone':self.telephone, 'email':self.email}
    
    
#modele medicament ndray mitahiry ny information mikasika ny  fanafody reetra ao anaty pharmacie
class Medicament(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)
    prix_achat = models.FloatField()
    prix_vente = models.FloatField()
    qte = models.IntegerField()
    fourniseur = models.ForeignKey(Fourniseur, on_delete=models.CASCADE)
    def medicament(self):
        return {'code':self.code, 'nom':self.nom, 'prix_achat':self.prix_achat, 'prix_vente':self.prix_vente, 'qte':self.qte, 'fourniseur':self.fourniseur}
   
#modele client ahafahana maka information mikasika ny client, 
# natao realise kokoa ilay izy hoe anarana no max alaina am client am resaka facture 
class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    
    def client(self):
        return {'id_client':self.id_client, 'nom':self.nom}


#ito ndray tableau commande ahafahana manao commande ny client eto no miasa ilay systeme de panier
#zany oe ito no mitondra ny zavatra reetra comandenn'ny client  de regrouper ato daholo 
class Commande(models.Model):
    id_commande = models.AutoField(primary_key=True)
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def commande(self):
        return {'id_commande':self.id_commande, 'date':self.date, 'client':self.client}
    
#ito ndray table manao relation amin'ny medicament sy commande no sad koa element anankiray ao anaty commande
#zany oe possible mividy fanafody samihafa de le izy element commande ray de mividy fanafody samihafa de otran ito maro2 no mifandray am comande

class Ventecli(models.Model):
    id_vente = models.AutoField(primary_key=True)
    qte = models.IntegerField()
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    somme = models.FloatField()
    def vente(self):
        return {'id_vente':self.id_vente, 'qte':self.qte, 'commande':self.commande, 'medicament':self.medicament, 'somme':self.somme}
 
#ito ndray table livraison ahafahana manao relation amin'ny fourniseur sy ny livraison anreo medicament ateriny
#miregouper maro2 koa ito zany oe achat fanafody maro2 no ato de amzay mora2 ny mijery livraison 
class Livraison(models.Model):
    id_livraison = models.AutoField(primary_key=True)
    date = models.DateField()
    fourniseur = models.ForeignKey(Fourniseur, on_delete=models.CASCADE)
    def livraison(self):
        return {'id_livraison':self.id_livraison, 'date':self.date, 'fourniseur':self.fourniseur}

# ireo fanafody zay nolivrena tao anty livraison iray, table maro2 otran ito no mifandray am livraison de lasa anankiray
class Achat(models.Model):
    id_achat = models.AutoField(primary_key=True)
    qte = models.IntegerField()
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    livraison = models.ForeignKey(Livraison, on_delete=models.CASCADE)
    somme = models.FloatField()
    def achat(self):
        return {'id_achat':self.id_achat, 'qte':self.qte, 'medicament':self.medicament, 'livraison':self.livraison, 'somme':self.somme}
    
    
#ito ndray table administrateur ahafahana manao relation amin'ny utilisateur sy ny user
class administrateur(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telephone = models.CharField(max_length=50)
    mdp = models.CharField(max_length=50)
    def asmin(self):
        return {'id_admin':self.id_admin, 'nom':self.nom, 'prenom':self.prenom, 'email':self.email, 'telephone':self.telephone, 'mdp':self.mdp}