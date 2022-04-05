from django import forms
from owner.models import Mobiles


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


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


