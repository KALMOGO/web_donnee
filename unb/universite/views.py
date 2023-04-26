from django.shortcuts import render

# Create your views here.

def Home_PageView(request):
    
    context = {"page_title": "Home Page"}
    
    return render(request, "index.html", context=context)

def Presentation_PageView(request):
    context={}
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