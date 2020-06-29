from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse

from online_market.users.forms import (
    UserRegisterForm, UserProfileForm, UserAddressForm
)

UserModel = get_user_model()


def register(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(
                request, 'register.html', {
                    'form': form,
                    'page_title': 'Online Market | Register'
                }
            )

    form = UserRegisterForm()
    return render(request, 'register.html', {
        'form': form,
        'page_title': 'Online Market | Register'
    })


@login_required(login_url='/users/login')
def profile_contacts(request: WSGIRequest) -> HttpResponse:
    if request.method == 'GET':
        form = UserProfileForm(instance=request.user)
        return TemplateResponse(
            request, template='profile.html', context={
                'form': form,
                'page_title': 'Online Market | Profile'
            }
        )
    else:
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return TemplateResponse(
            request, template='profile.html', context={
                'form': form,
                'page_title': 'Online Market | Profile',
                'is_updated': True,
            }
        )


@login_required(login_url='/users/login')
def profile_address(request: WSGIRequest) -> HttpResponse:
    if request.method == 'GET':
        form = UserAddressForm(instance=request.user.address)
        return TemplateResponse(
            request, template='profile_address.html', context={
                'form': form,
                'page_title': 'Online Market | Address'
            }
        )
    else:
        form = UserAddressForm(request.POST)
        if form.is_valid():
            address = form.save()
            request.user.address = address
            request.user.save()
        return TemplateResponse(
            request, template='profile_address.html', context={
                'form': form,
                'page_title': 'Online Market | Address',
                'is_updated': True,
            }
        )


def orders(request: WSGIRequest) -> HttpResponse:
    return TemplateResponse(request, template='orders.html', context={
        'orders': request.user.orders.all(),
        'page_title': 'Online Market | Orders',
    })
