from django.shortcuts import render

# Create your views here.
def place(request):
    return render("service1/place.html")

def player(request):
    return render("service1/player.html")