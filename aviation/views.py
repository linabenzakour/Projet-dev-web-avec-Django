from django.shortcuts import render, redirect,get_object_or_404
from .models import Avion, Aeroport
from .forms import AeroportForm, AvionForm
from django.core.exceptions import ValidationError

# Create your views here.

def data_list(request):
    avions = Avion.objects.all()
    aeroports = Aeroport.objects.all()
    return render(request, 'aviation/data_list.html', {'avions': avions, 'aeroports': aeroports})

def detail_avion(request, id_avion):
    avion = get_object_or_404(Avion, id_avion=id_avion)
    return render(request, 'aviation/detail_avion.html', {'avion': avion})

def detail_aeroport(request, id_aeroport):
    aeroport = get_object_or_404(Aeroport, id_aeroport=id_aeroport)
    return render(request, 'aviation/detail_aeroport.html', {'aeroport': aeroport})

def create_avion(request):
    if request.method == 'POST':
        form = AvionForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                
                avion = form.save()
                return redirect('detail_avion', id_avion=avion.id_avion)
            except ValidationError as e:
                
                return redirect('aeroport_plein')  
    else:
        form = AvionForm()

    return render(request, 'aviation/create_avion.html', {'form': form})


def ajouter_avion(request):
    if request.method == "POST":
        id_avion = request.POST.get("id_avion")
        compagnie = request.POST.get("compagnie")
        aeroport_id = request.POST.get("aeroport")
        
        try:
            aeroport = Aeroport.objects.get(id_aeroport=aeroport_id)

            
            if aeroport.is_occupied():
                raise ValidationError(f"L'aéroport {aeroport.id_aeroport} est plein.")

            
            avion = Avion(id_avion=id_avion, compagnie_aerienne=compagnie, lieu=aeroport)
            avion.save()

            return redirect("data_list") 

        except ValidationError as e:
            return render(request, "aviation/ajouter_avion.html", {"erreur": str(e)})
        except Aeroport.DoesNotExist:
            return render(request, "aviation/ajouter_avion.html", {"erreur": "Aéroport introuvable."})


    aeroports = Aeroport.objects.all()
    return render(request, "aviation/ajouter_avion.html", {"aeroports": aeroports})

def aeroport_plein(request):
    return render(request, 'aviation/aeroport_plein.html')


def create_aeroport(request):
    if request.method == 'POST':
        form = AeroportForm(request.POST, request.FILES)
        if form.is_valid():
            aeroport = form.save()  
            return redirect('detail_aeroport', id_aeroport=aeroport.id_aeroport) 
    else:
        form = AeroportForm()

    return render(request, 'aviation/create_aeroport.html', {'form': form})


def delete_aeroport(request, id_aeroport):
    aeroport = get_object_or_404(Aeroport, id_aeroport=id_aeroport)
    aeroport.delete()
    return redirect('data_list')

def delete_avion(request, id_avion):
    avion = get_object_or_404(Avion, id_avion=id_avion)
    avion.delete()
    return redirect('data_list')

def modify_avion(request, id_avion):
    avion = get_object_or_404(Avion, id_avion=id_avion)
    if request.method == 'POST':
        form = AvionForm(request.POST, instance=avion)
        if form.is_valid():
            form.save()
            return redirect('detail_avion', id_avion=id_avion)
    else:
        form = AvionForm(instance=avion)
    
    return render(request, 'aviation/modify_avion.html', {'form': form, 'avion': avion})

def modify_aeroport(request, id_aeroport):
    aeroport = get_object_or_404(Aeroport, id_aeroport=id_aeroport) 
    if request.method == 'POST':
        form = AeroportForm(request.POST, request.FILES, instance=aeroport)
        if form.is_valid():
            form.save() 
            return redirect('detail_aeroport', id_aeroport=aeroport.id_aeroport)  
    else:
        form = AeroportForm(instance=aeroport)

    return render(request, 'aviation/modify_aeroport.html', {'form': form})


def a_propos(request):
    return render(request, 'aviation/a-propos.html')

def base(request):
    return render(request, 'aviation/base.html')



