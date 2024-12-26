import random
from django.shortcuts import render
from Santa_list.models import SantaList
from Toy_factory.models import Toy,Coal
from django.contrib.auth.decorators import login_required

@login_required
def nice_naughty_statistics(request):
    santa_list = SantaList.objects.last()
    nice_count = santa_list.nice_list.count()
    naughty_count = santa_list.naughty_list.count()
    return render(request, 'nice_naughty_statistics.html',
    {'nice_count': nice_count, 'naughty_count': naughty_count})

@login_required
def toy_statistics(request):
    toys = Toy.objects.all()
    toy_count = {}
    for toy in toys:
        toy_count[toy.toy_type] = toy_count.get(toy.toy_type, 0) + 1
    return render(request, 'toy_statistics.html', {'toy_count': toy_count})

@login_required
def toy_creation_time(request):
    minutes_per_toy = random.randint(5, 15)
    toys = Toy.objects.all()
    toys_count =len(toys)
    total_time = toys_count * minutes_per_toy
    return render(request, 'toy_create_time.html',
    {'total_time': total_time,"toys_count":toys_count,"time":minutes_per_toy})

@login_required
def delivery_time(request):
    Delivery_time = random.randint(10, 50)
    toys = Toy.objects.all()
    punishment = Coal.objects.all()
    gift =len(toys) + len(punishment)
    total_time = gift * Delivery_time
    return render(request, 'deliver_time.html', {'total_time': total_time,"time":Delivery_time,"gift":gift})
