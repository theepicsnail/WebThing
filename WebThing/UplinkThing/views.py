# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import simplejson
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import *
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

        a = Agent()
        a.user=u
        a.money = 100
        a.save()

        s = Software(version=7,name="foo",cost=1000)
        s.save()

        c = Computer(speed=100, owner=a)
        c.software.add(s)
        c.save()

    except Exception, e:
        return e
    
    return None
def computer(request,cid,action):
    edit = False
    error= ""

    #find the computer
    try:
        comp = Computer.objects.get(cid=cid)
    except:
        error = "Could not find that computer."
        return render(request,"index.html",{"error":error}, context_instance=RequestContext(request))


    #if editing, make sure they are logged in
    if acction=="edit":
        user = request.session["user"]
        if not user:
            error = "You are not logged in."
        elif comp.owner != user:
            error = "This is not your computer"
        else:
            edit = True
            
            
    return render(request,"computer.html",{"computer":comp,
                                           "error":error,
                                           "edit":edit},
                  context_instance=RequestContext(request))

def terminal(request):
    return HTTPResponseRedirect("/index")
    
def upgrade(request):
    return HTTPResponseRedirect("/index")

def profileLookup(request):
    return render(request,"profileLookup.html",{})

def profile(request,name):
    return render(request,"profile.html",{"username":name,"error":str(request.session.keys())})

def ajax(request):
    d = {"a":1, 2:"c", "time":time.time(),"sess":str(request.session)}
    return HttpResponse(simplejson.dumps(d))

def logout(request):
    del request.session["user"]
    return HttpResponseRedirect("/index")

def login(request):
    if request.method == "GET":
        return HttpResponseRedirect("/index")
    user = authenticate(username=request.POST["username"], password=request.POST["password"])
    if user is not None:
        if user.is_active:
            request.session["user"]=user
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
    return render(request,"index.html",{},)
