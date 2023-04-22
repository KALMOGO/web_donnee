from django.shortcuts import render

# Create your views here.

def Home_PageView(request):
    
    context = {"page_title": "Home Page"}
    
    return render(request, "index.html", context=context)