from django import forms as dj_forms

from .utils import HyperviewRenderer

from django.forms.models import (
    BaseModelForm as DjBaseModelForm,
    ModelFormMetaclass as DjModelFormMetaclass,
)


class BaseForm(HyperviewRenderer, dj_forms.BaseForm):
    pass


class Form(HyperviewRenderer, dj_forms.Form):
    use_required_attribute = False


class BaseModelForm(DjBaseModelForm, BaseForm):
    pass


class ModelForm(BaseModelForm, metaclass=DjModelFormMetaclass):
    use_required_attribute = False
