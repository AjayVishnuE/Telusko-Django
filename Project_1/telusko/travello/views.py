from django.shortcuts import render
from .models import Destination


def index(request):
    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests' : dests})

def getlocationdet(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            D1=Destination()
            for i in Destination:
                if i.name==request.POST['name']:
                    D1.name=i.name
                    D1.img=i.img
                    D1.desc=i.desc
                    D1.price=i.price
            return render(request, 'loc_details.html',{'D1':D1})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'index.html')
