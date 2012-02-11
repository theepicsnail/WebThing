# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import login as , logout
from django.contrib.auth import authenticate
from django.utils import simplejson
import time


def handleRegister(postData):
    try: 
        Users.objects.get(username=postData["username"])
        return "That username is already being used."
    except:pass

    try:
        u = User.objects.create_user(
            username = postData["username"],
            password = postData["password"],
            email    = postData["email"])
        u.save()
    except Exception, e:
        return e
    
    return None

def profile(request,name):
    return render(request,"profile.html",{"username":name})

def ajax(request):
    d = {"a":1, 2:"c", "time":time.time()}    
    return HttpResponse(simplejson.dumps(d))

def logout(reuqest):
    return HttpResponseRedirect("/index")

def login(request):
    if request.method == "GET":
        return HttpResponseRedirect("/index")
    user = authenticate(username=request.POST["username"], password=request.POST["password"])
    if user is not None:
        if user.is_active:
            return HttpResponseRedirect("profile/"+user.username)
        else:
            return render(request,"index.html",{"error":"Your account is inactive."})
    return render(request,"index.html",{"error":"Invalid login."})

def register(request):
    error = None
    if request.method == "POST":
        error = handleRegister(request.POST)
        if not error:
            return HttpResponseRedirect("/index")
    return render(request,"register.html",{"error":error})

def index(request):
    return render(request,"index.html",{})
