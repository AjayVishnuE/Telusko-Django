from django.shortcuts import render
from .models import Destination
from django.contrib.auth.models import User, auth


def index(request):
    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests' : dests})

def getlocationdet(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            return render(request, 'loc_details.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'index.html')
