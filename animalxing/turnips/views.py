from django.shortcuts import render
from django.http import HttpResponse
from .models import Turnip_info
# Create your views here.

def index(request):
    latest_question_list = Turnip_info.objects.order_by('report_date')[:5]
    output = ', '.join([t_info.price for t_info in latest_question_list])


    return HttpResponse(output)

def best_price(request, date, isSell = False):
    response = "You're looking at the best price on %s."
    return  HttpResponse(response % date)

def input_price(request, date, isSell = False):
    return HttpResponse("You're inputting the price on %s." % date)