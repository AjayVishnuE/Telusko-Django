from django.shortcuts import render
from .models import Destination

def index(request):
    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = "The city that never sleeps"
    dest1.img = "destination_1.jpg"
    dest1.price = 900

    dest2 = Destination()
    dest2.name = "Kolkata"
    dest2.desc = "The city that is always alive"
    dest2.img = "destination_2.jpg"
    dest2.price = 1000

    dest3 = Destination()
    dest3.name = "Kochi"
    dest3.desc = "The city of love and food"
    dest3.img = "destination_3.jpg"
    dest3.price = 1300

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests' : dests})