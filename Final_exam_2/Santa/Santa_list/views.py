from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import SantaList, Kid
from .forms import KidForm
from django.contrib.auth.decorators import login_required


@login_required
def create_santas_list(request):
    santa_list = SantaList.objects.create()
    santa_list.create_santas_list()
    return redirect('view_santas_list')


@login_required
def view_santas_list(request):
    try:
        santa_list = SantaList.objects.last()
        naughty_kids = santa_list.naughty_list.all()
        nice_kids = santa_list.nice_list.all()
        return render(request, 'view_santa_list.html', {
            'naughty_kids': naughty_kids,
            'nice_kids': nice_kids
        })
    except SantaList.DoesNotExist:
        return HttpResponse("Santa's list not found", status=404)

@login_required
def create_kid(request):
    if request.method == 'POST':
        form = KidForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_all_kids")
    else:
        form = KidForm()
    return render(request, 'create_kid.html', {'form': form})

@login_required
def list_all_kids(request):
    kids = Kid.objects.all()
    return render(request, 'view_all_kid.html', {'kids': kids})

@login_required
def view_kid(request, id):
    kid = get_object_or_404(Kid, id=id)
    return render(request, 'view_kid.html', {'kid': kid})


@login_required
def remove_kid_from_list(request, kid_id):
    santa_list = SantaList.objects.last()
    kid = get_object_or_404(Kid, id=kid_id)
    if kid in santa_list.naughty_list.all():
        santa_list.naughty_list.remove(kid)
    elif kid in santa_list.nice_list.all():
        santa_list.nice_list.remove(kid)

    santa_list.save()
    return redirect('view_santas_list')


