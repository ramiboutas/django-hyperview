from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Contact
from .forms import ContactForm

from django_hv.http import hv_reponde


def contact_index(request):
    page = int(request.GET.get("page", 1))
    search = request.GET.get("q")
    if search:
        qs = Contact.objects.filter(
            Q(first_name__contains=search)
            | Q(last_name__contains=search)
            | Q(phone_number__contains=search)
            | Q(email__contains=search)
        )
    else:
        qs = Contact.objects.all()

    paginator = Paginator(qs, 10)
    rows_only = request.GET.get("rows_only") == "true"
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    template_name = "rows.xml" if rows_only else "index.xml"
    response = render(request, template_name, {"contacts": contacts})
    return hv_reponde(response)


def contact_detail(request, id):
    response = render(request, "show.xml", {"contact": Contact.objects.get(id=id)})
    return hv_reponde(response)


def contact_edit(request, id):
    contact = Contact.objects.get(id=id)
    form = ContactForm(request.POST or None, instance=contact)
    context = {"form": form, "contact": contact}
    if request.method == "GET":
        response = render(request, "edit.xml", context)
    elif request.method == "POST":
        if form.is_valid():
            form.save()
            context["saved"] = True
        response = render(request, "form_fields.xml", context)

    return hv_reponde(response)


def contact_delete(request, id):
    Contact.objects.get(id=id).delete()
    response = render(request, "deleted.xml")
    return hv_reponde(response)


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

    return hv_reponde(response)
