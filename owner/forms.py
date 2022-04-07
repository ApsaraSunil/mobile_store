from django import forms
from owner.models import Mobiles
from customer.models import Orders


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobiles
        fields = "__all__"
        widgets = {
            "mobile_name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "RAM_ROM": forms.TextInput(attrs={"class": "form-control"}),
            "processor": forms.TextInput(attrs={"class": "form-control"}),
            "rear_camera": forms.TextInput(attrs={"class": "form-control"}),
            "front_camera": forms.TextInput(attrs={"class": "form-control"}),
            "battery": forms.TextInput(attrs={"class": "form-control"}),
            "display": forms.TextInput(attrs={"class": "form-control"}),
            "stock": forms.NumberInput(attrs={"class": "form-control"})
        }

        def clean(self):
            cleaned_data = super(MobileForm, self).clean()
            price = cleaned_data.get("price")
            stock = cleaned_data.get("stock")
            if price < 0:
                msg = "invalid price"
                self.add_error("price", msg)
            if stock < 0:
                msg = "invalid stock"
                self.add_error("stock", msg)


class OrderEditForm(forms.ModelForm):
    options = (
        ("orderplaced", "orderplaced"),
        ("dispatched", "dispatched"),
        ("in_transmit", "in_transmit"),
        ("delivered", "delivered"),
    )
    status = forms.ChoiceField(choices=options, widget=forms.Select(attrs={"class": "form-select"}))

    class Meta:
        model = Orders
        fields = [
            "expected_delivery_date",
            "status"
        ]
        widgets = {
            "expected_delivery_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "status": forms.Select(attrs={"class": "form-select"})
        }

