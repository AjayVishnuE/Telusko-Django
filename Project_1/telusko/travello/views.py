from django.shortcuts import render
from .models import Destination
from django.contrib.auth.models import User, auth

def getspecificlocation(request):
    if request.method=="POST":
        # print(request.POST.get('dest-id'))
        x = request.POST.get('dest-id')
        print(x)
        if request.user.is_authenticated:
            dest=Destination.objects.filter(id=x)
            print (dest)
            return render(request, 'loc_details.html',{'dest':dest})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'index.html')


def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests' : dests})


