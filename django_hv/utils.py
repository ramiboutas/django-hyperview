from django.forms.utils import RenderableMixin


class HyperviewRenderer(RenderableMixin):
    template_name_view = "django_hv/forms/view.xml"
    template_name_label = "django_hv/forms/label.xml"

    def __str__(self):
        return self.render(self.template_name_view)

    def as_view(self):
        return self.render(self.template_name_view)
