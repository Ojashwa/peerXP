from django.shortcuts import render,HttpResponse,redirect
import json
from django.contrib import messages
import requests
from.models import Userlogin
from.forms import TokenForm

# Create your views here.
def login(request):
    '''insert the data to userlogin table in databse'''
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if Userlogin.objects.filter(email=email).exists():
            pass
        else:
            query = Userlogin(email=email,password=password,name=name)
            query.save(force_insert=True)
        request.session['username'] = name
        request.session['email'] = email
        messages.success(request,"Welcome "+name)
        return render(request,"index.html")
    return render(request,"login.html")
def index(request):

    return render(request,"index.html")

def tokens(request):
    '''This function handel the api request and show genrated tokens'''
    headers = {
                'orgId': '60001280952',
                'Authorization': '9446933330c7f886fbdf16782906a9e0',
                'Content-Type': 'application/json',
            }
    if request.method == 'POST':
        form = TokenForm(request.POST)
        # return HttpResponse(form)
        if form.is_valid():
            data = json.dumps(form.cleaned_data)
            print(type(data))
            print(data)
            
            #send the POST request to  inject data in API
            post_response = requests.post('https://desk.zoho.in/api/v1/tickets', headers=headers,data=data)
            #show response of POST
            print(post_response.status_code)
            #response save to post_token variable
            # post_token = post_response.json()
            messages.success(request,"Token created successfully")
            return redirect('tokens')
    #send GET request to API
    get_response = requests.get('https://desk.zoho.in/api/v1/tickets', headers=headers)
    # shows the response code of GET
    print(get_response.status_code)
    token_get = get_response.json()
    token_list = token_get['data']
    return render(request,"token_details.html",{'token_dict':token_list})

def token_details(request,tokenId_token):
    '''retrive specific ticket data'''
    token_Id = tokenId_token.split("_")[1]
    token = tokenId_token.split("_")[0]
    headers = {
                'orgId': '60001280952',
                'Authorization': '9446933330c7f886fbdf16782906a9e0',
                'Content-Type': 'application/json',
            }
    #send GET request to API
    get_response = requests.get('https://desk.zoho.in/api/v1/tickets/'+token_Id+'', headers=headers)
    # shows the response code of GET
    print(get_response.status_code)
    token_get = get_response.json()
    print(token_get)
    request.session['token'] = token
    return render(request,"tokens.html",{'token_get':token_get})
