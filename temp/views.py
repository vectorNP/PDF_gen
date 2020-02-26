from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf #created in step 4
from django.shortcuts import render, redirect


def get1(request):
    context = {
         
        "cust":[
            {"invoice_id":123,
            "customer_name":"John Copper",
            "amount":1399.99,
            "today":"Today"},
            {"invoice_id":123,
            "customer_name":"John Copper",
            "amount":1399.99,
            "today":"Today"},
            {"invoice_id":123,
            "customer_name":"John Copper",
            "amount":1399.99,
            "today":"Today"},
        ]
    }
    #use the below one to get html 
    #return render(request,'temp/invoice.html',context)

    #need to search the template in the temp/template folder 
    #otherwise it wont work
    pdf = render_to_pdf('temp/invoice.html',context)
    return HttpResponse(pdf,content_type='application/pdf')

