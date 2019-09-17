from django.shortcuts import render

# Create your views here.
def home_page(request):
    response = {"name": "Muh Riansyah"}
    return render(request, "homepage.html", response)
