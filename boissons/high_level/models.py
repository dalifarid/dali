from django.db import models
# models.IntegerField()
# models.CharField(max_length=100)
# models.ManyToManyField(Machine)
# models.ForeignKey(Local, on_delete=models.PROTECT,# blank=True, null=True, related_name="+",)


class MatierePremiere(models.Model):
    nom = models.IntegerField()
    stock = models.IntegerField()
    emprise = models.IntegerField()

    def __str__(self):
        return self.no


class QuantiteMatierePremiere(models.Model):
    quantite = models.IntegerField()
    matiere_premiere = models.ForeignKey(
        MatierePremiere,
        on_delete=models.PROTECT,
    )

    class Meta:
        abstract = True


class UtilisationMatierePremiere(QuantiteMatierePremiere):
    pass


class Localisation(models.Model):
    nom = models.IntegerField()
    taxes = models.IntegerField()
    prix_m2 = models.IntegerField()

    def __str__(self):
        return self.nom


class ApprovisionnementMatierePremiere(QuantiteMatierePremiere):
    localisation = models.ForeignKey(
        Localisation,
        on_delete=models.PROTECT,
    )
    prix_unitaire = models.IntegerField()
    delais = models.CharField(max_length=100)

    def __str__(self):
        return self.localisation


class Local(models.Model):
    nom = models.CharField(max_length=100)
    localisation = models.ForeignKey(
        Localisation,
        on_delete=models.PROTECT,
    )
    surface = models.IntegerField()

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix_de_vente = models.IntegerField()
    quantite = models.IntegerField()
    emprise = models.IntegerField()
    local = models.ForeignKey(
        Local,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.nom


class Energie(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    localisation = models.ForeignKey(
        Localisation,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.nom


class DebitEnergie(models.Model):
    debit = models.IntegerField()
    energie = models.ForeignKey(
        Energie,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.debit


class Metier(models.Model):
    nom = models.CharField(max_length=100)
    remuneration = models.IntegerField()

    def __str__(self):
        return self.nom


class RessourceHumaine(models.Model):
    metier = models.ForeignKey(
        Metier,
        on_delete=models.PROTECT,
    )
    quantite = models.IntegerField()

    def __str__(self):
        return self.nom


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix_achat = models.IntegerField()
    cout_maintenance = models.IntegerField()
    operateurs = models.ManyToManyField(RessourceHumaine)
    debit = models.IntegerField()
    surface = models.IntegerField()
    debit_energie = models.ForeignKey(
        DebitEnergie,
        on_delete=models.PROTECT,
    )
    taux_utilisation = models.IntegerField()
    local = models.ForeignKey(
        Local,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.nom


class Fabrication(models.Model):
    produit = models.ForeignKey(
        Produit,
        on_delete=models.PROTECT,
    )
    utilisations_matiere_premiere = models.ManyToManyField(UtilisationMatierePremiere)
    machines = models.ManyToManyField(Machine)
    ressources_humaines = models.ManyToManyField(RessourceHumaine)

    def __str__(self):
        return self.produit
