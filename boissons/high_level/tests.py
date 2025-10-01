# Create your tests here.
# from django.test import TestCase
from .models import Localisation, Local, Machine, MatierePremiere, ApprovisionnementMatierePremiere, DebitEnergie, Energie


from django.test import TestCase
from .models import Metier
class MachineModelTests(TestCase):
    def test_machine_creation(self):
        self.assertEqual(Metier.objects.count(), 0)
        Metier.objects.create(nom="plongeur", remuneration=10000, )
        self.assertEqual



class CostsTestCase(TestCase):
    def setUp(self):
        # Création de la localisation
        self.labege = Localisation.objects.create(nom="Labège", taxes=0, prix_m2=2000)
        # Création du local
        self.local = Local.objects.create(nom="LocalTest", localisation=self.labege, surface=50)
        # Machines
        energie = Energie.objects.create(nom="Electricité", prix=0, localisation=self.labege)  # localisation ajoutée
        debit = DebitEnergie.objects.create(debit=0, energie=energie)
        self.machine1 = Machine.objects.create(
            nom="Machine1", prix_achat=1000, cout_maintenance=0,
            debit=0, surface=0, debit_energie=debit,
            taux_utilisation=0, local=self.local
        )
        self.machine2 = Machine.objects.create(
            nom="Machine2", prix_achat=2000, cout_maintenance=0,
            debit=0, surface=0, debit_energie=debit,
            taux_utilisation=0, local=self.local
        )
        # Matière première
        sucre = MatierePremiere.objects.create(nom="Sucre", stock=1000, emprise=0)
        eau = MatierePremiere.objects.create(nom="Eau", stock=50, emprise=0)

        ApprovisionnementMatierePremiere.objects.create(
            quantite=1000, matiere_premiere=sucre,
            localisation=self.labege, prix_unitaire=10, delais="immédiat"
        )
        ApprovisionnementMatierePremiere.objects.create(
            quantite=50, matiere_premiere=eau,
            localisation=self.labege, prix_unitaire=15, delais="immédiat"
        )

    def test_local_costs(self):
        expected = 110750
        # Ici on additionne Local + Machines + Stock
        local_cost = self.local.costs()
        self.assertEqual(local_cost, expected)

