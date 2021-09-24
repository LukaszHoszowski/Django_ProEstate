from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from Building.models import Building, Flat, BuildingDocs


class BuildingListView(LoginRequiredMixin, ListView):
    model = Building
    context_object_name = 'buildings'
    paginate_by = 8
    template_name = 'Building/buildings.html'


class BuildingDetailView(LoginRequiredMixin, DetailView):
    model = Building
    context_object_name = 'building'
    template_name = 'Building/building_details.html'
    slug_field = 'slug'


class BuildingDetailDocsView(LoginRequiredMixin, ListView):
    model = BuildingDocs
    context_object_name = 'building'
    template_name = 'Building/building_details.html'


class BuildingDetailPhotosView(LoginRequiredMixin, ListView):
    model = BuildingDocs
    context_object_name = 'building'
    template_name = 'Building/building_details.html'


class FlatListView(LoginRequiredMixin, ListView):
    model = Flat
    context_object_name = 'flats'
    paginate_by = 3
    template_name = 'Building/flats.html'


class FlatDetailView(LoginRequiredMixin, DetailView):
    model = Flat
    context_object_name = 'flat'
    template_name = 'Building/flat_details.html'
    slug_field = 'slug'
