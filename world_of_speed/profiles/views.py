from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from world_of_speed.common.profile_helpers import get_profile
from world_of_speed.profiles.models import Profile


class ProfileCreateView(views.CreateView):
    model = Profile
    template_name = 'profile/profile-create.html'
    fields = ["username", "email", "age", "password"]
    success_url = reverse_lazy('catalogue')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['password'].widget = forms.PasswordInput()
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_profile()
        return context


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        cars = profile.car_set.all()
        total_prices = sum([car.price for car in cars])
        context['total_prices'] = total_prices
        return context


class ProfileDeleteView(views.DeleteView):
    model = Profile
    template_name = "profile/profile-delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()


class ProfileEditView(views.UpdateView):
    model = Profile
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('profile details')
    fields = "__all__"

    def get_object(self, queryset=None):
        return get_profile()

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields['age'].help_text = ''
        return form
