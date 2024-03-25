from django.shortcuts import render
from django.views import generic as views

from world_of_speed.common.profile_helpers import get_profile


# Create your views here.
class IndexView(views.TemplateView):
    template_name = 'web/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_profile()
        return context
