from django.http import request
from django.shortcuts import render, reverse, redirect
from .models import Product
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from account.models import CustomUser
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'shop/product_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'shop/product_detail.html', context)


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    model = Product
    fields = ('title', 'category', 'price', 'description')
    template_name = 'shop/product_update.html'

    def test_func(self):
        return self.request.user.is_employee or self.request.user.is_staff


class ProdcutCreateView(UserPassesTestMixin, CreateView):
    model = Product
    fields = ('title', 'category', 'price', 'description')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(ProdcutCreateView, self).form_invalid(form)

    def test_func(self):
        return self.request.user.is_staff

    template_name = 'shop/product_create.html'


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'shop/product_delete.html'
    success_url = reverse_lazy('account:user_profile')

    def test_func(self):
        return self.request.user.is_staff
