from django.shortcuts import render,HttpResponse,redirect
from.models import Userlogin


# Create your views here.
def login(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if Userlogin.objects.filter(email=email).exists:
            pass
        else:
            query = Userlogin(email=email,password=password,name=name)
            query.save(force_insert=True)
        request.session['username'] = name
        request.session['email'] = email

        return redirect('index')
    return render(request,"login.html")
def index(request):
    return render(request,"index.html")