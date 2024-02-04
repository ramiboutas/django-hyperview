from .models import Contact

from django_hv.forms import ModelForm
from django_hv import widgets


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "phone_number", "email")
        widgets = {
            "first_name": widgets.TextField(attrs={"placeholder": "First name"}),
            "last_name": widgets.TextField(attrs={"placeholder": "Last name"}),
            "phone_number": widgets.TextField(attrs={"placeholder": "Phone number"}),
            "email": widgets.TextField(attrs={"placeholder": "Email address"}),
            "contact_type": widgets.PickerField({}),
            "active": widgets.Switch("Activate"),
        }
