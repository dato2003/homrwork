from django.shortcuts import render, redirect
from .models import Toy, Coal
from Santa_list.models import Kid, SantaList
from django.contrib.auth.decorators import login_required

@login_required
def create_toy(request):
        santa_lists = SantaList.objects.all()
        for santa_list in santa_lists:
            for kid in santa_list.nice_list.all():
                if not Toy.objects.filter(kid=kid).exists():
                    Toy.objects.create(kid=kid, toy_type=kid.gift)

            for kid in santa_list.naughty_list.all():
                if not Coal.objects.filter(kid=kid).exists():
                    Coal.objects.create(kid=kid)

        return redirect("generate_gift")

@login_required
def view_toy(request, kid_id):
    toy = Toy.objects.get(kid__id=kid_id)
    return render(request, 'view_toy.html', {'toy': toy})

@login_required
def generate_gift(request):
    toys = Toy.objects.all()
    coal = Coal.objects.all()
    punishment = Coal.punishment
    return render(request, 'view_all_toys.html', {'toys': toys, "coal": coal, "punishment": punishment})


@login_required
def view_all_toys(request):
    toys = Toy.objects.all()
    return render(request, 'view_all_toys.html', {'toys': toys,})


