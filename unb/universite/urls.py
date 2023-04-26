from django.urls import path, include
from .views import *


urlpatterns = [
    path("", Home_PageView, name='home'),
    path("actualite/", Actualite_PageView, name='actualite'),
    path("actualite/<int:id>/detail", Actualite_Detail_PageView, name='_actualite_detail'),
    path("formation/", Formation_PageView, name='formation'),
    path("etablissement/home/", Etablissement_PageView, name='etablissement_home'),
    path("etablissement/", Home_etablissement_PageView, name='etablissement'),
    path("laboratoire/", Laboratoire_PageView, name='laboratoire'),
    path("partenaire/", Partenaire_PageView, name='partenaire'),
    path("site/", Site_PageView, name='site'),
    path("ecole_doctorale/", EcoleDoctorale_PageView, name='ecole_doctorale'),
    path("ecole_doctorale_home/", Home_ecole_doctorale_PageView, name='ecole_doctorale_home'),
    path("document/", Document_PageView, name='document'),
    path("presentation/", Presentation_PageView, name='presentation'),
    path("recherche/", Recherche_PageView, name="recherche")
]
