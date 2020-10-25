from django.shortcuts import render,HttpResponse
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
    if request.method == 'POST':
        form = TokenForm(request.POST)
        if form.is_valid():
            # data = form.cleaned_data
            # print(data)
            headers = {
                'orgId': '60001280952',
                'Authorization': '9446933330c7f886fbdf16782906a9e0',
            }
            # data comes from the form in this format
            
            # data = '{ "subCategory" : "demo", "cf" : { "cf_permanentaddress" : null, "cf_dateofpurchase" : null, "cf_phone" : null, "cf_numberofitems" : null, "cf_url" : null, "cf_secondaryemail" : null, "cf_severitypercentage" : "0.0", "cf_modelname" : "F3 2017" }, "productId" : "", "contactId" : "1892000000042032", "subject" : "Real Time analysis Requirement", "dueDate" : "2016-06-21T16:16:16.000Z", "departmentId" : "1892000000006907", "channel" : "Email", "description" : "demo", "language" : "English", "priority" : "High", "classification" : "", "assigneeId" : "1892000000056007", "phone" : "1 888 900 9646", "category" : "demo", "email" : "demo@gmail.com", "status" : "Open" }'
            data = '{ "Department" : "Sub General","Category" : "demo" ,"PWSLab Project URL" : "https://company.pwslab.net/johndoe/my-project/" ,"Subject" : "subject" , "Description" : "this is description" ,"Contact_Name" : "demo" ,"Email" : "demo@gmail.com" ,"Priority" : "Low - General Guidance"}'
            # will send GET request to API
            response = requests.post('https://desk.zoho.in/api/v1/tickets', headers=headers,data=data)
            # response = requests.get('https://desk.zoho.in/api/v1/tickets', headers=headers)
            # shows the response code
            print("============",response.status_code)
            token = response.json()
            # print(token)
            # token_dict = token['data']
            # print("====>",token['data'])
            return render(request,"token_details.html")
    return render(request,"token_details.html")