from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, DeleteView, UpdateView, CreateView
from owner.forms import MobileForm, LoginForm
from owner.models import Mobiles
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from owner.decorators import admin_sign_in_required
from django.utils.decorators import method_decorator


# Create your views here.


# class SigninView(View):
#     def get(self, request, *args, **kwargs):
#         form = LoginForm
#         return render(request, "signin.html", {"form": form})
#
#     def post(self, request, *args, **kwargs):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 print("login success")
#                 login(request, user)
#                 return redirect("list_mobiles")
#             else:
#                 print("login failed")
#                 return render(request, "signin.html", {"form": form})

@method_decorator(admin_sign_in_required, name="dispatch")
class AddMobileView(CreateView):
    model = Mobiles
    form_class = MobileForm
    template_name = "add_mobiles.html"
    success_url = reverse_lazy("list_mobiles")


@method_decorator(admin_sign_in_required, name="dispatch")
class MobileListView(ListView):
    model = Mobiles
    template_name = "mobile_list.html"
    context_object_name = "mobiles"


@method_decorator(admin_sign_in_required, name="dispatch")
class MobileDetailView(DetailView):
    model = Mobiles
    template_name = "mobile_detail.html"
    context_object_name = "mobile"


@method_decorator(admin_sign_in_required, name="dispatch")
class MobileEditView(UpdateView):
    model = Mobiles
    form_class = MobileForm
    template_name = "edit_mobile.html"
    success_url = reverse_lazy("list_mobiles")
    pk_url_kwarg = "id"


@method_decorator(admin_sign_in_required, name="dispatch")
class MobileDeleteView(DeleteView):
    model = Mobiles
    template_name = "delete_mobile.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("list_mobiles")


@admin_sign_in_required
def signout(request, *args, **kwargs):
    logout(request)
    return redirect("signin")
