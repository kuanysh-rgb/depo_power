from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Locomotive, TechWork, MonthWorkDay, AvailableTechwork, Canava, CellRecord


# Create your views here.

def main(request):
    loco_data = Locomotive.objects.all()
    month_data = MonthWorkDay.objects.all()
    techwork_data = TechWork.objects.all()
    available_techworks = AvailableTechwork.objects.all()
    canava1 = Canava.objects.filter(place_row=1).order_by('place_column')
    canava2 = Canava.objects.filter(place_row=2).order_by('place_column')
    canava3 = Canava.objects.filter(place_row=3).order_by('place_column')
    cell_records_jan = CellRecord.objects.filter(month=1)
    cell_records_feb = CellRecord.objects.filter(month=2)
    cell_records_mar = CellRecord.objects.filter(month=3)
    cell_records_apr = CellRecord.objects.filter(month=4)
    cell_records_may = CellRecord.objects.filter(month=5)
    cell_records_jun = CellRecord.objects.filter(month=6)
    cell_records_jul = CellRecord.objects.filter(month=7)
    cell_records_aug = CellRecord.objects.filter(month=8)
    cell_records_sep = CellRecord.objects.filter(month=9)
    cell_records_oct = CellRecord.objects.filter(month=10)
    cell_records_nov = CellRecord.objects.filter(month=11)
    cell_records_dec = CellRecord.objects.filter(month=12)

    sum_jan = cell_records_jan.aggregate(Sum('volume')).get('volume__sum', 0.00)
    sum_feb = cell_records_feb.aggregate(Sum('volume')).get('volume__sum', 0.00)
    sum_mar = cell_records_mar.aggregate(Sum('volume')).get('volume__sum', 0.00)
    sum_apr = cell_records_apr.aggregate(Sum('volume')).get('volume__sum', 0.00)
    sum_may = cell_records_may.aggregate(Sum('volume')).get('volume__sum', 0.00)
    sum_jun = cell_records_jun.aggregate(Sum('volume')).get('volume__sum', 0.00)
    sum_jul = cell_records_jul.aggregate(Sum('volume')).get('volume__sum', 0.00)
    sum_aug = cell_records_aug.aggregate(Sum('volume')).get('volume__sum', 0.00)
    sum_sep = cell_records_sep.aggregate(Sum('volume')).get('volume__sum', 0.00)
    sum_oct = cell_records_oct.aggregate(Sum('volume')).get('volume__sum', 0.00)
    sum_nov = cell_records_nov.aggregate(Sum('volume')).get('volume__sum', 0.00)
    sum_dec = cell_records_dec.aggregate(Sum('volume')).get('volume__sum', 0.00)

    st_dni_jan = 0
    for cellrecordjan in cell_records_jan:
        norm = TechWork.objects.values('norms_in_days').filter(model_name=cellrecordjan.locomotive, to_name=cellrecordjan.techwork)
        st_dni_jan += float(cellrecordjan.volume) * norm[0].get('norms_in_days')
    st_dni_jan = int(140 - st_dni_jan)

    st_dni_feb = 0
    for cellrecordfeb in cell_records_feb:
        norm = TechWork.objects.values('norms_in_days').filter(model_name=cellrecordfeb.locomotive,
                                                               to_name=cellrecordfeb.techwork)
        st_dni_feb += float(cellrecordfeb.volume) * norm[0].get('norms_in_days')
    st_dni_feb = int(140 - st_dni_feb)

    st_dni_mar = 0
    for cellrecordmar in cell_records_mar:
        norm = TechWork.objects.values('norms_in_days').filter(model_name=cellrecordmar.locomotive,
                                                               to_name=cellrecordmar.techwork)
        st_dni_mar += float(cellrecordmar.volume) * norm[0].get('norms_in_days')
    st_dni_mar = int(140 - st_dni_mar)

    st_dni_apr = 0
    for cellrecordapr in cell_records_apr:
        norm = TechWork.objects.values('norms_in_days').filter(model_name=cellrecordapr.locomotive,
                                                               to_name=cellrecordapr.techwork)
        st_dni_apr += float(cellrecordapr.volume) * norm[0].get('norms_in_days')
    st_dni_apr = int(140 - st_dni_apr)

    st_dni_may = 0
    for cellrecordmay in cell_records_may:
        norm = TechWork.objects.values('norms_in_days').filter(model_name=cellrecordmay.locomotive,
                                                               to_name=cellrecordmay.techwork)
        st_dni_may += float(cellrecordmay.volume) * norm[0].get('norms_in_days')
    st_dni_may = int(140 - st_dni_may)

    st_dni_jun = 0
    for cellrecordjun in cell_records_jun:
        norm = TechWork.objects.values('norms_in_days').filter(model_name=cellrecordjun.locomotive,
                                                               to_name=cellrecordjun.techwork)
        st_dni_jun += float(cellrecordjun.volume) * norm[0].get('norms_in_days')
    st_dni_jun = int(140 - st_dni_jun)

    st_dni_jul = 0
    for cellrecordjul in cell_records_jul:
        norm = TechWork.objects.values('norms_in_days').filter(model_name=cellrecordjul.locomotive,
                                                               to_name=cellrecordjul.techwork)
        st_dni_jul += float(cellrecordjul.volume) * norm[0].get('norms_in_days')
    st_dni_jul = int(140 - st_dni_jul)

    st_dni_aug = 0
    for cellrecordaug in cell_records_aug:
        norm = TechWork.objects.values('norms_in_days').filter(model_name=cellrecordaug.locomotive,
                                                               to_name=cellrecordaug.techwork)
        st_dni_aug += float(cellrecordaug.volume) * norm[0].get('norms_in_days')
    st_dni_aug = int(140 - st_dni_aug)

    st_dni_sep = 0
    for cellrecordsep in cell_records_sep:
        norm = TechWork.objects.values('norms_in_days').filter(model_name=cellrecordsep.locomotive,
                                                               to_name=cellrecordsep.techwork)
        st_dni_sep += float(cellrecordsep.volume) * norm[0].get('norms_in_days')
    st_dni_sep = int(140 - st_dni_sep)

    st_dni_oct = 0
    for cellrecordoct in cell_records_oct:
        norm = TechWork.objects.values('norms_in_days').filter(model_name=cellrecordoct.locomotive,
                                                               to_name=cellrecordoct.techwork)
        st_dni_oct += float(cellrecordoct.volume) * norm[0].get('norms_in_days')
    st_dni_oct = int(140 - st_dni_oct)

    st_dni_nov = 0
    for cellrecordnov in cell_records_nov:
        norm = TechWork.objects.values('norms_in_days').filter(model_name=cellrecordnov.locomotive,
                                                               to_name=cellrecordnov.techwork)
        st_dni_nov += float(cellrecordnov.volume) * norm[0].get('norms_in_days')
    st_dni_nov = int(140 - st_dni_nov)

    st_dni_dec = 0
    for cellrecorddec in cell_records_dec:
        norm = TechWork.objects.values('norms_in_days').filter(model_name=cellrecorddec.locomotive,
                                                               to_name=cellrecorddec.techwork)
        st_dni_dec += float(cellrecorddec.volume) * norm[0].get('norms_in_days')
    st_dni_dec = int(140 - st_dni_dec)

    total = 7
    if Canava.objects.filter(machine='Свободно').count() == 7:
        percentage = 0
    else:
        inwork = total - Canava.objects.filter(machine='Свободно').count()
        percentage = (inwork / total) * 100
        percentage = round(percentage, 2)

    percentage_jan = ((140-st_dni_jan)/140) * 100
    percentage_jan = round(percentage_jan, 2)

    percentage_feb = ((140 - st_dni_feb) / 140) * 100
    percentage_feb = round(percentage_feb, 2)

    percentage_mar = ((140 - st_dni_mar) / 140) * 100
    percentage_mar = round(percentage_mar, 2)

    percentage_apr = ((140 - st_dni_apr) / 140) * 100
    percentage_apr = round(percentage_apr, 2)

    percentage_may = ((140 - st_dni_may) / 140) * 100
    percentage_may = round(percentage_may, 2)

    percentage_jun = ((140 - st_dni_jun) / 140) * 100
    percentage_jun = round(percentage_jun, 2)

    percentage_jul = ((140 - st_dni_jul) / 140) * 100
    percentage_jul = round(percentage_jul, 2)

    percentage_aug = ((140 - st_dni_aug) / 140) * 100
    percentage_aug = round(percentage_aug, 2)

    percentage_sep = ((140 - st_dni_sep) / 140) * 100
    percentage_sep = round(percentage_sep, 2)

    percentage_oct = ((140 - st_dni_oct) / 140) * 100
    percentage_oct = round(percentage_oct, 2)

    percentage_nov = ((140 - st_dni_nov) / 140) * 100
    percentage_nov = round(percentage_nov, 2)

    percentage_dec = ((140 - st_dni_dec) / 140) * 100
    percentage_dec = round(percentage_dec, 2)

    percentage = (percentage_jan + percentage_feb + percentage_mar + percentage_apr + percentage_may + percentage_jun + percentage_jul + percentage_aug + percentage_sep + percentage_oct + percentage_nov + percentage_dec)/12
    percentage = round(percentage, 2)
    return render(request, 'depopower/index.html', {'loco_data': loco_data, 'month_data': month_data,
                                                    'techwork_data': techwork_data,
                                                    'available_techworks': available_techworks,
                                                    'canava1': canava1, 'canava2': canava2, 'canava3': canava3,
                                                    'percentage': percentage,
                                                    'cell_records_jan': cell_records_jan,
                                                    'cell_records_feb': cell_records_feb,
                                                    'cell_records_mar': cell_records_mar,
                                                    'cell_records_apr': cell_records_apr,
                                                    'cell_records_may': cell_records_may,
                                                    'cell_records_jun': cell_records_jun,
                                                    'cell_records_jul': cell_records_jul,
                                                    'cell_records_aug': cell_records_aug,
                                                    'cell_records_sep': cell_records_sep,
                                                    'cell_records_oct': cell_records_oct,
                                                    'cell_records_nov': cell_records_nov,
                                                    'cell_records_dec': cell_records_dec,
                                                    'sum_jan': sum_jan,
                                                    'sum_feb': sum_feb,
                                                    'sum_mar': sum_mar,
                                                    'sum_apr': sum_apr,
                                                    'sum_may': sum_may,
                                                    'sum_jun': sum_jun,
                                                    'sum_jul': sum_jul,
                                                    'sum_aug': sum_aug,
                                                    'sum_sep': sum_sep,
                                                    'sum_oct': sum_oct,
                                                    'sum_nov': sum_nov,
                                                    'sum_dec': sum_dec,
                                                    'st_dni_jan': st_dni_jan,
                                                    'st_dni_feb': st_dni_feb,
                                                    'st_dni_mar': st_dni_mar,
                                                    'st_dni_apr': st_dni_apr,
                                                    'st_dni_may': st_dni_may,
                                                    'st_dni_jun': st_dni_jun,
                                                    'st_dni_jul': st_dni_jul,
                                                    'st_dni_aug': st_dni_aug,
                                                    'st_dni_sep': st_dni_sep,
                                                    'st_dni_oct': st_dni_oct,
                                                    'st_dni_nov': st_dni_nov,
                                                    'st_dni_dec': st_dni_dec,
                                                    'percentage_jan': percentage_jan,
                                                    'percentage_feb': percentage_feb,
                                                    'percentage_mar': percentage_mar,
                                                    'percentage_apr': percentage_apr,
                                                    'percentage_may': percentage_may,
                                                    'percentage_jun': percentage_jun,
                                                    'percentage_jul': percentage_jul,
                                                    'percentage_aug': percentage_aug,
                                                    'percentage_sep': percentage_sep,
                                                    'percentage_oct': percentage_oct,
                                                    'percentage_nov': percentage_nov,
                                                    'percentage_dec': percentage_dec,
                                                    })


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


def edit(request):
    return render(request, 'depopower/edit.html')
