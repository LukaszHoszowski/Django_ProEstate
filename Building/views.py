from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from Building.models import Building


class BuildingListView(LoginRequiredMixin, ListView):
    model = Building
    context_object_name = 'buildings'
    paginate_by = 3
    template_name = 'Building/buildings.html'


class BuildingDetailView(LoginRequiredMixin, DetailView):
    model = Building
    context_object_name = 'building'
    template_name = 'Building/building_details.html'
