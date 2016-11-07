from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse

from order_form.forms import MyForm

def hello(request):
    return HttpResponse('Hello, lady!')

def index(request):
    if request.method == 'GET':
        return render(request, 'order_form/index.html')


class MyView(View):
    def get(self, request):
        form = MyForm()
        c = {'form': form}
        return render(request, 'order_form/form.html', c)

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your order is placed')
        else:
            messages.error(request, 'Validation failed')
        c = {'form': form}
        return render(request, 'order_form/form.html', c)