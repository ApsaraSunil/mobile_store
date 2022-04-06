from django.shortcuts import render, redirect
from owner.models import Mobiles
from django.views.generic import View, CreateView, ListView, DetailView, TemplateView
from customer.forms import UserRegistrationForm, LoginForm, PasswordResetForm, OrderForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from customer.models import Cart, Orders, Profile
from customer.decorators import sign_in_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.db.models import Sum


# Create your views here.


class SignupView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "signup.html"
    success_url = reverse_lazy("signin")


class SigninView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm
        return render(request, "signin.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user:
                print("login success")
                login(request, user)

                if request.user.is_superuser:
                    return redirect("list_mobiles")
                else:
                    return redirect("cust_home")
            else:
                print("login failed")
                return render(request, "signin.html", {"form": form})


@method_decorator(sign_in_required, name="dispatch")
class PasswordResetView(View):
    def get(self, request):
        form = PasswordResetForm
        return render(request, "password_reset.html", {"form": form})

    def post(self, request):
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data.get("old_password")
            new_password = form.cleaned_data.get("new_password")
            user = authenticate(request, username=request.user, password=old_password)
            if user:
                user.set_password(new_password)
                user.save()
                return redirect("signin")
            else:
                return render(request, "password_reset.html", {"form": form})
        else:
            return render(request, "password_reset.html", {"form": form})


@method_decorator(sign_in_required, name="dispatch")
class CustomerIndex(ListView):
    model = Mobiles
    template_name = "cust_home.html"
    context_object_name = "mobiles"


@method_decorator(sign_in_required, name="dispatch")
class MobileDetailView(DetailView):
    model = Mobiles
    template_name = "detail_view.html"
    context_object_name = "mobile"
    pk_url_kwarg = "id"


@sign_in_required
def add_to_cart(request, *args, **kwargs):
    mobile = Mobiles.objects.get(id=kwargs["id"])
    user = request.user
    cart = Cart(product=mobile,
                user=user)
    cart.save()
    messages.success(request, "item has been added to cart")
    return redirect("cust_home")


@method_decorator(sign_in_required, name="dispatch")
class ViewMyCart(ListView):
    model = Cart
    template_name = "my_cart.html"
    context_object_name = "carts"

    # def get_queryset(self):
    def get(self, request, *args, **kwargs):
        qs = self.model.objects.filter(user=self.request.user).exclude(status="cancelled").order_by("-date")

        total_sum = qs.aggregate(Sum("product__price"))
        total = total_sum["product__price__sum"]

        context = {"carts": qs, "total": total}
        return render(request, self.template_name, context)


@sign_in_required
def remove_cart_item(request, *args, **kwargs):
    cart = Cart.objects.get(id=kwargs["id"])
    cart.status = "cancelled"
    cart.save()
    messages.error(request, "item has been deleted")
    return redirect("cust_home")


@method_decorator(sign_in_required, name="dispatch")
class OrderCreateView(CreateView):
    form_class = OrderForm
    template_name = "order_create.html"
    model = Orders

    def post(self, request, *args, **kwargs):
        cart_id = kwargs.get("c_id")
        product_id = kwargs.get("p_id")
        form = OrderForm(request.POST)

        if form.is_valid():
            cart = Cart.objects.get(id=cart_id)
            address = form.cleaned_data.get("address")
            product = Mobiles.objects.get(id=product_id)
            user = request.user
            order = Orders(product=product, user=user, address=address)
            order.save()
            cart.status = "order_placed"
            cart.save()
            messages.success(request, "your order has been placed")
            return redirect('cust_home')


@method_decorator(sign_in_required, name="dispatch")
class OrderListView(ListView):
    model = Orders
    template_name = "order_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Orders.objects.filter(user=self.request.user).order_by("-date")


@sign_in_required
def cancel_order(request, *args, **kwargs):
    o_id = kwargs.get("id")
    order = Orders.objects.get(id=o_id)
    order.status = "order_cancelled"
    order.save()
    messages.success(request, "your order is cancelled")
    return redirect("cust_home")


@method_decorator(sign_in_required, name="dispatch")
class ProfileView(CreateView):
    model = Profile
    template_name = "profile.html"
    form_class = ProfileForm

    def post(self, request):
        form = self.form_class(request.POST, files=request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("cust_home")
        else:
            return render(request, self.template_name, {"form": form})



@method_decorator(sign_in_required, name="dispatch")
class MyProfileView(TemplateView):
    template_name = "my_profile.html"


@sign_in_required
def signout(request, *args, **kwargs):
    logout(request)
    return redirect("signin")
