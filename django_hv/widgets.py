from django.forms.widgets import Widget, ChoiceWidget, CheckboxInput

from django.conf import settings


class TextField(Widget):
    """
    Base class for a <text-field> widget.

    https://hyperview.org/docs/reference_textfield
    """

    template_name = "django_hv/forms/widgets/text-field.xml"


class SelectSingle(ChoiceWidget):
    """
    Base class for a <select-single> widget.

    https://hyperview.org/docs/reference_selectsingle
    """

    template_name = "django_hv/forms/widgets/select-single.xml"
    option_template_name = "django_hv/forms/widgets/option.xml"
    checked_attribute = {"selected": False}
    option_inherits_attrs = False


class SelectMultiple(ChoiceWidget):
    """
    Base class for a <select-multiple> widget.

    https://hyperview.org/docs/reference_selectmultiple
    """

    template_name = "django_hv/forms/widgets/select-multiple.xml"
    option_template_name = "django_hv/forms/widgets/option.xml"
    checked_attribute = {"selected": False}
    option_inherits_attrs = False


class PickerField(ChoiceWidget):
    """
    Base class for a <picker-field> widget.

    https://hyperview.org/docs/reference_pickerfield
    """

    template_name = "django_hv/forms/widgets/picker-field.xml"
    option_template_name = "django_hv/forms/widgets/picker-item.xml"
    checked_attribute = {"selected": False}
    option_inherits_attrs = False

    def __init__(self, label_text=None, attrs=None):
        super().__init__(attrs)
        self.label_text = label_text

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["label_text"] = self.label_text
        return context


class Switch(Widget):
    """
    Base class for a <switch> widget.

    https://hyperview.org/docs/reference_switch
    """

    template_name = "django_hv/forms/widgets/switch.xml"

    def __init__(self, label_text=None, attrs=None):
        super().__init__(attrs)
        self.label_text = label_text

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["label_text"] = self.label_text
        return context


class DateField(Widget):
    """
    Base class for a <date-field> widget.

    https://hyperview.org/docs/reference_datefield
    """

    label_format = getattr(settings, "HYPERVIEW_DATEFIELD_FORMAT", "MMMM D, YYYY")
    template_name = "django_hv/forms/widgets/date-field.xml"

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["label_format"] = self.label_format
        return context
