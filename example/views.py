from django.views.generic import TemplateView
from example.models import Color
from django.http import Http404


class ColorsPageView(TemplateView):
    template_name = "example/colors.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        colors = Color.objects.all()
        data["colors"] = colors
        return data


class ColorPageView(TemplateView):
    template_name = "example/color.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        try:
            color = Color.objects.get(uuid=kwargs["uuid"])
        except Color.DoesNotExist:
            raise Http404("Color not found")
        data["color"] = color
        return data
