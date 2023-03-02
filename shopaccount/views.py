from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.db.models import Q
from filter_and_pagination import FilterPagination
from .models import Marketplace, Transaction
from .forms import MarketplaceForm, TransactionForm
from .serializers import TransactionSerializer, MarketplaceSerializer

def create_view(request, data):
    # dictionary for initial data with
    # field names as keys
    context ={}; data_mp = {}
 
    if data == '1':
        # add the dictionary during initialization
        form = MarketplaceForm(request.POST or None)
    else:
        data_mp = Marketplace.objects.all()
        form = TransactionForm(request.POST or None) 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(settings.BASE_LINK+"/list_view")

         
    context['form'] = form
    resultset = {
        'dataset': data,
        'data_mp': data_mp,
        'context': context
    }

    return render(request, "create_view.html", resultset)

def list_view(request):
    url = settings.BASE_LINK
    return render(request, "list_view.html", {'url':url})

def detail_view(request, id, data):
    context = {}
    context["data"] = Marketplace.objects.get(id = id)
    return render(request, "detail_view.html", {'data_id':id, 'data_no': data, 'context': context})

def list_marketplace(request):
    queryset = Marketplace.objects.all()
    context  = MarketplaceSerializer(queryset, many=True).data
    resultset = {'dataset':context}

    return JsonResponse(resultset, safe=False)

def list_transaction(request, start_date, end_date):
    # dictionary for initial data with
    # field names as keys
    # add the dictionary during initialization
    queryset = Transaction.objects.all().order_by('date')
    if (start_date!='-' and end_date!='-'):
        queryset = Transaction.objects.filter(date__range=[start_date, end_date]).order_by('-date')

    context = TransactionSerializer(queryset, many=True).data      
    resultset = {'dataset': context}

    return JsonResponse(resultset, safe=False)


def list_detail(request, id, data, start_date, end_date):
    # dictionary for initial data with
    # field names as keys
    context = {}
    data_list = {}
    _basic_price = 0
    _total_profit = 0
    _total_qty = 0
    _total_selling_price = 0
    _total_basic_price = 0
    mp = ""; tr = ""

    if data=='1':
        # add the dictionary during initialization
        context["data"] = Marketplace.objects.get(id = id)
        data_list['dataset'] = Transaction.objects.filter(mp_id = context["data"].id).order_by('-date')
        if (start_date!='-' and end_date!='-'):
            data_list['dataset'] = Transaction.objects.filter(mp_id = context["data"].id, date__range=[start_date, end_date]).order_by('-date')
        #_total_qty = Transaction.objects.aggregate(Sum('quantity'))['quantity__sum']
        #_total_selling_price = Transaction.objects.aggregate(Sum('selling_price'))['selling_price__sum']
        #_total_basic_price = Transaction.objects.aggregate(Sum('basic_price'))['basic_price__sum']
        
        mp = MarketplaceSerializer(context["data"], many=False).data
        tr = TransactionSerializer(data_list['dataset'], many=True).data 

        for _data_list in data_list['dataset']:
            _total_qty += _data_list.quantity
            _total_selling_price += _data_list.selling_price
            _total_basic_price += _data_list.basic_price
            _basic_price = _data_list.quantity * _data_list.basic_price
            _total_profit += _data_list.selling_price - _basic_price
    else:
        context["data"] = Transaction.objects.get(id = id)
        tr = TransactionSerializer(context["data"], many=False).data

    resultset = {
                    'marketplace': mp, 
                    'transaction': tr, 
                    'total_profit':_total_profit, 
                    'total_qty':_total_qty,
                    'total_selling_price':_total_selling_price,
                    'total_basic_price':_total_basic_price
                }

    return JsonResponse(resultset, safe=False)

# update view for details
def update_view(request, id, data):
    # dictionary for initial data with
    # field names as keys
    context = {}
    data_mp = {}
    data_mp_id = {}
    data_trx = {}
    date_format = settings.DATE_INPUT_FORMATS
 
    if data=='1':
        # fetch the object related to passed id
        # obj = get_object_or_404(Marketplace, id = id)
        data_mp_id = Marketplace.objects.get(id = id)
     
        # pass the object as instance in form
        form = MarketplaceForm(request.POST or None, instance = data_mp_id)
    else:
        # fetch the object related to passed id
        data_mp = Marketplace.objects.all()
        data_trx = Transaction.objects.get(id = id)
     
        # pass the object as instance in form
        form = TransactionForm(request.POST or None, instance = data_trx)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(settings.BASE_LINK+"/list_view")
 
    # add form dictionary to context
    context["form"] = form
    resultset = {
                    'dataset':data, 
                    'data_trx': data_trx, 
                    'data_mp': data_mp, 
                    'data_mp_id': data_mp_id,
                    'formset':context
                }

    return render(request, "update_view.html", resultset)

def delete_item(request, id):
    # fetch the object related to passed id
    obj = get_object_or_404(Marketplace, id = id)
 
    if request.method =="POST":
        # delete object
        obj.delete()
        return HttpResponseRedirect("../list_view")
 
    return render(request, "list_view.html", {'delete_mp_item': True, 'item_id': id})

# def filtering(request):
#     queryset = FilterPagination.filter_and_pagination(request, Transaction)
#     serialize_data = TransactionSerializer(queryset['queryset'], many=True).data
      
#     resultset = {'dataset': serialize_data, 'pagination': queryset['pagination']}

#     return JsonResponse(resultset, safe=False)