from django.shortcuts import render

# Create your views here.

def home(request):#whenver we are clicking on a url we are making a
    return render(request, 'pages/home.html')#render means throwing
def about(request):
    return render(request, 'pages/about.html')
def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request , 'pages/contact.html')
