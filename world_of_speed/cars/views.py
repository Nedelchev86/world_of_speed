from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from world_of_speed.cars.forms import CarDeleteForm
from world_of_speed.cars.models import Car
from world_of_speed.common.profile_helpers import get_profile


# Create your views here.
class CatalogueView(views.ListView):
    model = Car
    template_name = "car/catalogue.html"


class CarCreateView(views.CreateView):
    model = Car
    template_name = "car/car-create.html"
    fields = ["type", "model", "year", "image_url", "price"]
    success_url = reverse_lazy("catalogue")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['image_url'].widget.attrs['placeholder'] = 'https://...'
        return form

    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk
        return super().form_valid(form)


class CarDetailsView(views.DetailView):
    model = Car
    template_name = "car/car-details.html"


class CarEditView(views.UpdateView):
    model = Car
    template_name = "car/car-edit.html"
    fields = ["type", "model", "year", "image_url", "price"]
    success_url = reverse_lazy("catalogue")


class CarDeleteView(views.DeleteView):
    model = Car
    template_name = "car/car-delete.html"
    success_url = reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CarDeleteForm(instance=self.object)

        return context
