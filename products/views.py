from django.shortcuts import render
from django.core import serializers
from .models import Products, ProductsCategory
from django.http import HttpResponse
from django.views.generic import View, DetailView
# Create your views here.


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


class ProductsHome(View):
    def get(self, request):
        if is_ajax(request):
            x = request.GET.get('value', 6)
            if Products.objects.order_by('id').filter(category=2).count() - (int(x) + 6) >= 0:
                y = int(x) + 6
            else:
                y = Products.objects.order_by('id').filter(category=2).count()
            data = serializers.serialize(
                'json', Products.objects.filter(status=True).filter(category=2).order_by('id')[int(x):int(y)])
            return HttpResponse(data, content_type='application/json')

        else:
            products = Products.objects.filter(
                status=True).filter(category=2).order_by('id')[0:6]
            products_count = Products.objects.filter(
                status=True).filter(category=2).order_by('id').count()
            products_status = products_count > 6
            return render(request, 'products/products.html', {'products': products, 'count': products_count, 'products_status': products_status})


class ProductsView(DetailView):
    model = Products
    template_name = 'products/products_detail.html'
    context_object_name = 'product'
