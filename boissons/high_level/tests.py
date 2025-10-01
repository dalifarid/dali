# Create your tests here.


from django.test import TestCase
from .models import Metier
class MachineModelTests(TestCase):
    def test_machine_creation(self):
        self.assertEqual(Metier.objects.count(), 0)
        Metier.objects.create(nom="plongeur", remuneration=10000, )
        self.assertEqual