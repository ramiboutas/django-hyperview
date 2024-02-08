# django-hyperview 

Django extensions for Hyperview mobile apps


## Installation and Setup

### Install with pip

``` sh
python -m pip install django-hyperview
```

### Configure

Add the app, once installed, to your `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...
    "django_hv",
    ...
]
```

Optionally, you can add the `HyperviewMiddleware` middleware to your settings.

```python
MIDDLEWARE = [
    ...
    "django_hv.middleware.HyperviewMiddleware",
]
```


## Usage


### xml-based form fields


As with Django, you can dynamically create your xml-based forms with this package.

```python
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
        }

```


In your view you can initiate the form as usual:

```python
def contact_new(request):
    context = {"form": ContactForm(request.POST or None)}
    if request.method == "GET":
        response = render(request, "new.xml", context)
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            context["saved"] = True
            context["contact"] = form.save()
        response = render(request, "form_fields.xml", context)
    return hv_repond(response)

```

And the xml template, you can render the form as follows:

```xml
{% load hv_tags %}
<view xmlns="https://hyperview.org/hyperview" style="edit-group">
{% if saved %}
  <behavior trigger="load" once="true" action="dispatch-event" event-name="contact-updated" />
  <behavior trigger="load" once="true" action="reload" href="{{ contact.detail_url }}" />
{% endif %}
{% hv_csrf_token request %}
{{ form }}
</view>

```



Note that you can create a CSRF token if you load the template tags of this package: `{% hv_csrf_token request %}`. It needs the `request` as an argument since Django requires that object to create a token.

### Hyperview response



You can use this package for your views.


```python

from .models import Contact
from .forms import ContactForm

from django_hv.http import hv_repond

def contact_detail(request, id):
    response = render(request, "show.xml", {"contact": Contact.objects.get(id=id)})
    return hv_repond(response)

```



### Check if the request comes from a Hypermedia client

For this to work, you need to add `HyperviewMiddleware` to `MIDDLEWARE`.


```python
def contact_detail(request, id):
    template = "show.xml" if request.hv else "show.html"
    response = render(request, template, {"contact": Contact.objects.get(id=id)})
    return hv_repond(response)


```


The property `request.hv` checks if the request has a specific header that is passed by the Hypermedia client.