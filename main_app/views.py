from django.shortcuts import render


# from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hello Robert in TIETO</h1>')
    name = 'Gold nugget'
    value = 1000.00
    context = {'treasure_name': name,
               'treasure_val': value}
    return render(request, 'index.html', {'treasures': treasures})


class Treasure:
    def __init__(self, name, value, material, location):
        self.name = name
        self.value = value
        self.material = material
        self.location = location


treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Golden Gates, Frisco, CA"),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO"),
    Treasure('Coffee Cup', 2, 'coffee', 'Office, Wroclaw, PL')
]
