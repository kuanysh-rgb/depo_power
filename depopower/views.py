from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Locomotive, TechWork, MonthWorkDay, AvailableTechwork, Canava


# Create your views here.

def main(request):
    loco_data = Locomotive.objects.all()
    month_data = MonthWorkDay.objects.all()
    techwork_data = TechWork.objects.all()
    available_techworks = AvailableTechwork.objects.all()
    canava1 = Canava.objects.filter(place_row=1).order_by('place_column')
    canava2 = Canava.objects.filter(place_row=2).order_by('place_column')
    canava3 = Canava.objects.filter(place_row=3).order_by('place_column')

    total = 7
    if Canava.objects.filter(machine='Свободно').count() == 7:
        percentage = 0
    else:
        inwork = total - Canava.objects.filter(machine='Свободно').count()
        percentage = (inwork / total) * 100
        percentage = round(percentage, 2)

    return render(request, 'depopower/index.html', {'loco_data': loco_data, 'month_data': month_data,
                                                    'techwork_data': techwork_data,
                                                    'available_techworks': available_techworks,
                                                    'canava1': canava1, 'canava2': canava2, 'canava3': canava3,
                                                    'percentage': percentage})


def add(request, to_name):
    loco_data = Locomotive.objects.all()
    month_data = MonthWorkDay.objects.all()
    techwork_data = TechWork.objects.all()
    available_techworks = AvailableTechwork.objects.all()
    canava1 = Canava.objects.filter(place_row=1).order_by('place_column')
    canava2 = Canava.objects.filter(place_row=2).order_by('place_column')
    canava3 = Canava.objects.filter(place_row=3).order_by('place_column')
    send_to_name = to_name
    return render(request, 'depopower/add.html', {'loco_data': loco_data, 'month_data': month_data,
                                                  'techwork_data': techwork_data,
                                                  'available_techworks': available_techworks,
                                                  'canava1': canava1, 'canava2': canava2, 'canava3': canava3,
                                                  'send_to_name': send_to_name})


