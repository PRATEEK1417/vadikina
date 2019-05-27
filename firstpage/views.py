from functools import wraps
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import *
from django.http import HttpResponse,HttpResponseRedirect
from requests import HTTPError
from django.shortcuts import render
import pyrebase
import random
import json



config = {
    'apiKey': "AIzaSyASBF-CxE7mZEyMvDYgXE-7c-9_6AlBUaU",
    'authDomain': "vadikina-5ffc0.firebaseapp.com",
    'databaseURL': "https://vadikina-5ffc0.firebaseio.com",
    'projectId': "vadikina-5ffc0",
    'storageBucket': "vadikina-5ffc0.appspot.com",
    'messagingSenderId': "738018847589"
  }

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

def logout_required(function):
    @wraps(function)
    def wrapper(request,*args, **kwargs):
        print (auth.current_user)
        if auth.current_user is  None:
            return HttpResponseRedirect('/firstpage/index/')
        else:
            return function(request,*args, **kwargs)
    return wrapper



def index(request):

    return render(request,"index.html")

def post_login(request):

    username = request.POST.get('email')
    passsword = request.POST.get('password')
    user=auth.sign_in_with_email_and_password(username,passsword)
    uid = auth.current_user["localId"]

    print(uid)
    return HttpResponseRedirect("/firstpage/home/")

@logout_required
def home(request):

    data = dict(db.child("products").get().val())

    return render(request,"home.html",{"products":data})

def search(request):
    search = request.GET.get('search')
    return HttpResponse()

def addproduct(request):


    return render(request,"addproduct.html")

def products(request):
    product_category=request.POST.get('product_category')
    product_name = request.POST.get('product_name')
    available_quantity = request.POST.get('available_quantity')
    single_button = request.POST.get('single_button')
    pid =random.randint(1000,9999)
    db.child("products").child(pid).update({"name":product_name,"category":product_category,"quantity":available_quantity,})

    return HttpResponseRedirect("/firstpage/home/")



def sign_up(request):
    return render(request,"signup1.html")

def post_sign_up(request):
    username = request.POST.get('email')
    print(username)
    password = request.POST.get('password')
    print(password)
    name=request.POST.get('name')
    phonenumber=request.POST.get('phonenumber')
    auth.create_user_with_email_and_password(username,password)
    auth.sign_in_with_email_and_password(username,password)
    uid= auth.current_user["localId"]
    db.child("users").child(uid).update({"phonenumber":phonenumber,"name":name})
    return HttpResponseRedirect("/firstpage/home/")




def log_out(request):

    auth.current_user=None

    return HttpResponseRedirect("/firstpage/index/")


def cart(request):
    uid = auth.current_user["localId"]
    cart_details=dict(db.child("users").child(uid).child("cart").get().val())
    del_items
    return render(request,"cart.html",{"products":cart_details})

def add_cart(request):
    pid = request.GET.get("id")

    uid = auth.current_user["localId"]
    print(uid)
    db.child("users").child(uid).child("cart").update({"product_id":pid})
    return HttpResponse(json.dumps({"data":True}))

def del_from_cart(request):
    uid = auth.current_user["localId"]
    del_item=dict(db.child("users").child(uid).child("cart").remove())
    return HttpResponse(json.dumps({"data":True}))



