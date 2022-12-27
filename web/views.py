from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from web.forms import SigninForm, CreateUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Event, Order
from .forms import EventForm
from django.contrib import messages
from web import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
import requests
User = get_user_model()


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def create_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return ("an 'invalid login' error message")
    context = {"form": form}
    return render(request, "create_user.html", context)


def signout_user(req):
    logout(req)
    return redirect("home")


def signin_user(req):
    form = SigninForm()
    if req.method == "POST":
        form = SigninForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(req, auth_user)
                return redirect("home")
    context = {"form": form}
    return render(req, "signin.html", context)


@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile-update')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'profile_update.html', {'user_form': user_form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = "change_password.html"
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')


def get_Orders(req):

    response = requests.get('http://127.0.0.1:8000/list/order/')

    orders = response.json()

    _orders = []

    for order in orders:

        _orders.append(

            {

                "id": order['id'],

                "user": order['user'],

                "carType": order['carType'],

                "fuelType": order['fuelType'],

                "litter": order['litter'],

                "address": order['address'],

                "date": order['date'],

                "time": order['time'],

                "price": order['price'],

                "payed": order['payed'],

                "status": order['status'],

                "extraService": order['extraService'],



            }

        )

    context = {"orders": _orders}

    return render(req, "order_list.html", context)


def get_order(req, order_id):

    response = requests.get(
        'http://127.0.0.1:8000/get/order/' + str(order_id) + '/')

    order = response.json()

    print(order)

    # user_count=User.objects.annotate=Count('bookingstatus',filter=Q(bookingstatus="yes"))

    context = {

        "order": {

            "id": order[0]['id'],

            "user": order[0]['user'],

            "carType": order[0]['carType'],

            "fuelType": order[0]['fuelType'],

            "litter": order[0]['litter'],

            "address": order[0]['address'],

            "date": order[0]['date'],

            "time": order[0]['time'],

            "price": order[0]['price'],

            "payed": order[0]['payed'],

            "status": order[0]['status'],

            "extraService": order[0]['extraService'],

        }



    }

    return render(req, "order_detail.html", context)


def confirm_order(request, order_id):

    response = requests.put(
        'http://127.0.0.1:8000/edit/order/' + str(order_id) + '/', {'status': 'true'})

    order = response.json()

    print(order)

    return get_order(request, order_id)
