from django import forms as dj_forms

from . import widgets


class Field(dj_forms.Field):
    widget = widgets.TextField


class TextField(Field, dj_forms.CharField):
    widget = widgets.TextField


class MultilineTextField(Field, dj_forms.Textarea):
    widget = widgets.TextField(attrs={"multiline": "true"})


class Switch(Field, dj_forms.CheckboxInput):
    widget = widgets.Switch


class DateField(Field, dj_forms.DateInput):
    widget = widgets.DateField


class SelectSingle(Field, dj_forms.RadioSelect):
    widget = widgets.SelectSingle


class PickerField(Field, dj_forms.RadioSelect):
    widget = widgets.PickerField


class SelectMultiple(Field, dj_forms.SelectMultiple):
    widget = widgets.SelectMultiple
