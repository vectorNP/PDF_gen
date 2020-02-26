from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf #created in step 4
from django.shortcuts import render, redirect


def get1(request):
    context = {
         "invoice_id":123,
         "customer_name":"John Copper",
         "amount":1399.99,
         "today":"Today",
    }
    return render(request,'temp/invoice.html',context)
