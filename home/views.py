from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import  messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is homepage")

def about(request):
    #return HttpResponse("This is aboutpage")    
    return render(request , 'about.html')

def contact(request):
    if request.method == 'POST':
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        Address = request.POST.get('address')
        Address2 = request.POST.get('address2')
        City = request.POST.get('city')
        State = request.POST.get('state')
        Zip = request.POST.get('zip')
        contact = Contact(email = Email, password = Password, address = Address, address2 = Address2, city = City, state = State,zip = Zip, date = datetime.today())
        contact.save()
        messages.success(request,"Form has been submitted")
    return render(request , 'contact.html')
    # return HttpResponse('This is contact page')