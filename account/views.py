from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from .models import CustomUser
from .forms import CustomerSignupForm, EmployeeSignupForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from shop.models import Product



def user_profile(request):
    all_product = Product.objects.all()
    context = {
        'all_product': all_product
    }
    return render(request, 'account/user_profile.html', context)


class RegistrationView(TemplateView):
    template_name = 'registration.html'


class CustomerRegistrationView(CreateView):
    model = CustomUser
    form_class = CustomerSignupForm
    template_name = 'account/customer_registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class EmployeeRegistrationView(CreateView):
    model = CustomUser
    form_class = EmployeeSignupForm
    template_name = 'account/employee_registration.html'

    def form_valid(self, form, backend='django.contrib.auth.backends.ModelBackend'):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if '@' in cd['username']:
                username = CustomUser.objects.get(email=cd['username']).username
            else:
                username = cd['username']

            user = authenticate(username=username,
                                password=cd['password'])

            if user is not None and user.is_active:
                login(request, user)
                return redirect('shop:product-list')
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
