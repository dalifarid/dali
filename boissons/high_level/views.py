# Create your views here.

from django.views.generic.detail import DetailView
from django.http import JsonResponse
from .models import (
    MatierePremiere,
    QuantiteMatierePremiere,
    UtilisationMatierePremiere,
    Localisation,
    ApprovisionnementMatierePremiere,
    Local,
    Produit,
    Energie,
    DebitEnergie,
    Metier,
    RessourceHumaine,
    Machine,
    Fabrication
)

class JSONDetailView(DetailView):
    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.toJSON(), safe=False)


class MatierePremiereDetailView(JSONDetailView):
    model = MatierePremiere


class QuantiteMatierePremiereDetailView(JSONDetailView):
    model = QuantiteMatierePremiere


class UtilisationMatierePremiereDetailView(JSONDetailView):
    model = UtilisationMatierePremiere


class LocalisationDetailView(JSONDetailView):
    model = Localisation


class ApprovisionnementMatierePremiereDetailView(JSONDetailView):
    model = ApprovisionnementMatierePremiere


class LocalDetailView(JSONDetailView):
    model = Local


class ProduitDetailView(JSONDetailView):
    model = Produit


class EnergieDetailView(JSONDetailView):
    model = Energie


class DebitEnergieDetailView(JSONDetailView):
    model = DebitEnergie


class MetierDetailView(JSONDetailView):
    model = Metier


class RessourceHumaineDetailView(JSONDetailView):
    model = RessourceHumaine


class MachineDetailView(JSONDetailView):
    model = Machine


class FabricationDetailView(JSONDetailView):
    model = Fabrication
