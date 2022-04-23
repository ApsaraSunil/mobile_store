from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, DeleteView, UpdateView, CreateView, TemplateView
from owner.forms import MobileForm, OrderEditForm
from owner.models import Mobiles
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from owner.decorators import admin_sign_in_required
from django.utils.decorators import method_decorator
from customer.models import Orders
from django.core.mail import send_mail


# Create your views here.


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
    pk_url_kwarg = "id"


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


@method_decorator(admin_sign_in_required, name="dispatch")
class DashBoardView(TemplateView):
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        new_orders = Orders.objects.filter(status="orderplaced")
        return render(request, self.template_name, {"new_orders": new_orders})


@method_decorator(admin_sign_in_required, name="dispatch")
class OrderDetailView(DetailView):
    model = Orders
    template_name = "order_detail.html"
    context_object_name = "order"
    pk_url_kwarg = "id"


@method_decorator(admin_sign_in_required, name="dispatch")
class OrderEditView(UpdateView):
    model = Orders
    template_name = "order_edit.html"
    form_class = OrderEditForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("order_detail")

    def get(self, request, *args, **kwargs):
        order = Orders.objects.get(id=kwargs["id"])
        return render(request, self.template_name, {"order": order, "form": self.form_class})

    def post(self, request, *args, **kwargs):
        order = Orders.objects.get(id=kwargs["id"])
        form = OrderEditForm(request.POST, instance=order)
        if form.is_valid():
            expected_delivery_date = form.cleaned_data.get("expected_delivery_date")
            form.save()
            send_mail(
                'Order notification',
                'Your order will be delivered on ' + str(expected_delivery_date),
                'apsarasunil333@gmail.com',
                ['aravindsunil94@gmail.com'],
                fail_silently=False,
            )
            return redirect("dashboard")


@admin_sign_in_required
def signout(request, *args, **kwargs):
    logout(request)
    return redirect("signin")
