from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views.generic import ListView
from . import forms

def hello_world(request):
    contexto = {'username': 'Aluno Django'}
    return render(request, 'hello.html', contexto)

def product_list_simple(request):
    products = models.Product.objects.all()
    product_names = "<br>".join([product.name for product in products])
    return HttpResponse(product_names)

def contact_view(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, 'contact_success.html', {'name': name, 'email': email})
    else:
        form = forms.ContactForm()

    return render(request, 'contact-register.html', {'form': form})

def products_create_view(request):
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return render(request, 'product_success.html', {'product': product})
    else:
        form = forms.ProductForm()

    return render(request, 'product_create.html', {'form': form})

class ProductListView(ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        return models.Product.objects.all().order_by('name')