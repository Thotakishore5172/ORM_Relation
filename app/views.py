from django.shortcuts import render

# Create your views here.
from app.models import *

def display_user(request):
    DUN=User.objects.all()
    d={'DUN':DUN}

    return render(request,'display_user.html',d)
