from django.shortcuts import render


def main(request):
    return render(request, "theme/main.html")

def login(request):
    return render(request, 'theme/login.html')

def signup(request):
    return render(request, 'theme/signup.html')

# Create your views here.
