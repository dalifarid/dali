"""
URL configuration for boissons project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path


from .views import (
    MatierePremiereDetailView,
    QuantiteMatierePremiereDetailView,
    UtilisationMatierePremiereDetailView,
    LocalisationDetailView,
    ApprovisionnementMatierePremiereDetailView,
    LocalDetailView,
    ProduitDetailView,
    EnergieDetailView,
    DebitEnergieDetailView,
    MetierDetailView,
    RessourceHumaineDetailView,
    MachineDetailView,
    FabricationDetailView
)

urlpatterns = [
    path('matiere_premiere/<int:pk>/', MatierePremiereDetailView.as_view(), name='matiere-detail'),
    path('quantite_matiere_premiere/<int:pk>/', QuantiteMatierePremiereDetailView.as_view(), name='quantite-detail'),
    path('utilisation_matiere_premiere/<int:pk>/', UtilisationMatierePremiereDetailView.as_view(), name='utilisation-detail'),
    path('localisation/<int:pk>/', LocalisationDetailView.as_view(), name='localisation-detail'),
    path('approvisionnement/<int:pk>/', ApprovisionnementMatierePremiereDetailView.as_view(), name='approvisionnement-detail'),
    path('local/<int:pk>/', LocalDetailView.as_view(), name='local-detail'),
    path('produit/<int:pk>/', ProduitDetailView.as_view(), name='produit-detail'),
    path('energie/<int:pk>/', EnergieDetailView.as_view(), name='energie-detail'),
    path('debit_energie/<int:pk>/', DebitEnergieDetailView.as_view(), name='debit-detail'),
    path('metier/<int:pk>/', MetierDetailView.as_view(), name='metier-detail'),
    path('ressource_humaine/<int:pk>/', RessourceHumaineDetailView.as_view(), name='ressource-detail'),
    path('machine/<int:pk>/', MachineDetailView.as_view(), name='machine-detail'),
    path('fabrication/<int:pk>/', FabricationDetailView.as_view(), name='fabrication-detail'),
]
