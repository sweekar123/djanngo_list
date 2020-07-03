from django.shortcuts import render,redirect
from .models import people
from django.contrib import messages
from django.contrib.auth.models import User,auth
import requests
import json
# Create your views here.

def portfolio(request):
	return render(request,'mysite/portfolio.html')	

 
def p_signin(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password_1 = request.POST['password1']
		password_2 = request.POST['password2']
		address = request.POST['address']
		city = request.POST['city']

		if password_1 == password_2:

			if people.objects.filter(username = username).exists():
				messages.info(request,'Username exists choose another')
				return redirect('people_signin')

			elif people.objects.filter(email = email).exists():
				messages.info(request,'email already exists')
				return redirect('people_signin')

			else:
			   people.objects.create(first_name = first_name, last_name = last_name,username = username, email = email, password = password_1, address = address, city = city)
			   
			   print('people created')

		else:
		  messages.info(request,"password isn't matching ")
		  return redirect('people_signin')
		  return redirect('/')	
	else:
	   return render(request,'mysite/people_signin.html')	 


def u_signin(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password_1 = request.POST['password1']
		password_2 = request.POST['password2']

		if password_1 == password_2:
			if User.objects.filter(username = username).exists():
				messages.info(request," Error !!! Username already exists")
				return redirect('user_signin')

			elif User.objects.filter(email = email).exists():
			      messages.info(request," Error !!! Email already exists")
			      return redirect('user_signin')

			else:
			   User.objects.create_user(first_name = first_name , last_name = last_name , username = username ,email = email , password = password_1)
			   print("User created")

		else:
		   messages.info(request," Error !!! Password not matching")
		   return redirect('user_signin')
		   return redirect('/')

	else:
	   return render(request,'mysite/user_signin.html')


def about(request):
	 return render(request,'mysite/about.html')     



def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password =request.POST['password']
        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
             messages.info(request,'invalid credentials')
             return redirect('login')    
    else:
        return render(request,'mysite/login.html')  


def logout(request):
    auth.logout(request)
    return redirect('/')        



def index(request):
	if request.method == 'POST' :
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']

		r = requests.get('http://api.icndb.com/jokes/random?firstName='+ first_name + '&lastName=' +last_name)
		json_data = json.loads(r.text)
		joke = json_data.get('value').get('joke')
		context = { 'joke' : joke}

		return render(request,'mysite/index.html',context)

	else:
		first_name = 'Albert'
		last_name = 'Einstein'

		r = requests.get('http://api.icndb.com/jokes/random?firstName='+ first_name + '&lastName=' +last_name)
		json_data = json.loads(r.text)
		joke = json_data.get('value').get('joke')
		context = {'joke' : joke }

		return render(request,'mysite/index.html',context)	
