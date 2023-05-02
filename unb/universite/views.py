from django.shortcuts import render
import owlready2 as owl
from .models import Ontology
# Create your views here.

ontology = Ontology()

def Home_PageView(request):
    
    data = {"page_title": "Home Page"}
    president = ontology.getPresident()
    actualities = ontology.getActualities()
    partenaire = ontology.getPartenaire()
    enseignants = ontology.getEnseignant()
    formations = ontology.getEtablissement()
    
    universite = ontology.getUniversite()
    data.update({"actualities":actualities})
    data.update({"universite":universite})
    data.update({"president":president})
    data.update({"partenaire":partenaire})
    data.update({"enseignants":enseignants})
    data.update({"formations":formations})
    return render(request, "index.html", context=data)

def Presentation_PageView(request):
    universite = ontology.getUniversite()
    context={"universite":universite}
    return render(request, "presentation.html", context=context)

def Recherche_PageView(request):
    context={}
    return render(request, "recherche.html", context=context)

def Actualite_PageView(request):
    
    context = {}
    return render(request, "actualite.html", context=context)

def Formation_PageView(request):
    context = {}
    return render(request, "formation.html", context=context)


def Etablissement_PageView(request):
    context = {}
    return render(request, "etablissement.html", context=context)


def Home_etablissement_PageView(request):
    context = {}
    return render(request, "home_etablissement.html", context=context)


def Laboratoire_PageView(request):
    context = {}
    return render(request, "laboratoire.html", context=context)


def Partenaire_PageView(request):
    context = {}
    return render(request, "partenaire.html", context=context)


def Site_PageView(request):
    context = {}
    return render(request, "site.html", context=context)


def EcoleDoctorale_PageView(request):
    context = {}
    return render(request, "ecole_doctorale.html", context=context)

def Home_ecole_doctorale_PageView(request):
    context = {}
    return render(request, "home_ecole_doctorale.html", context=context)

def Document_PageView(request):
    context = {}
    return render(request, "document.html", context=context)


def Actualite_Detail_PageView(request):
    context = {}
    return render(request, "actualite_detail.html", context=context)

