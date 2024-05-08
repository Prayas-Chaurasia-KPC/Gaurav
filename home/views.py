from django.shortcuts import render, HttpResponse, redirect
from .models import ContactUs

def index(request):
    context={
        "variable":"this is sent"
    }
    return render(request,'index.html',context)
   # return HttpResponse("Hello World")

def about(request):
    return render(request,'about.html')
   # return HttpResponse("about page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("service page")

def contact(request):
    if request.method == "POST":
        obj = ContactUs(name=request.POST["name"],
                       email=request.POST["email"],
                       phone=request.POST["phone"],
                       msg=request.POST["msg"])
        obj.save()
        return redirect("index")
    return render(request,'contact.html')
    

