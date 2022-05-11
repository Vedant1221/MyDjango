from django.shortcuts import render
from .models import C_gallery

 
def index(request):
    return render(request,'index.html')
# Create your views here.
 
def AboutMe(request):
    return render(request,"AboutMe.html")
 
def JavaScript(request):
    return render(request,"JavaScript.html")
 
def login(request):
    return render(request,"login.html")
 
def gallery(request):
    gal_obj = C_gallery.objects.all()
    return render(request,'gallery.html', {'gal_obj':gal_obj} )
 
def contact(request):
    return render(request,"contact.html")
 
