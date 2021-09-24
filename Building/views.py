from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from Building.forms import BuildingPhotosForm
from Building.models import Building, Flat, BuildingDocs, BuildingPhotos


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


class BuildingCartographyView(LoginRequiredMixin, DetailView):
    model = Building
    context_object_name = 'building'
    template_name = 'Building/building_cartography.html'
    slug_field = 'slug'


class BuildingCoopView(LoginRequiredMixin, DetailView):
    model = Building
    context_object_name = 'building'
    template_name = 'Building/building_coop.html'
    slug_field = 'slug'


class BuildingDocsView(LoginRequiredMixin, ListView):
    model = Building
    context_object_name = 'building'
    template_name = 'Building/building_documents.html'
    slug_field = 'slug'


class BuildingPhotosView(LoginRequiredMixin, DetailView):
    model = Building
    context_object_name = 'building'
    template_name = 'Building/building_photos.html'
    slug_field = 'slug'


class BuildingPhotosCreate(LoginRequiredMixin, CreateView):
    form_class = BuildingPhotosForm
    template_name = 'Building/building_photos_create.html'
    success_url = reverse_lazy('Building:building_photos')

    def form_valid(self, form):
        building = Building.objects.get(slug=self.kwargs['slug'])
        self.object = form.save(commit=False)
        self.object.building = building
        return super().form_valid(form)

    def get_initial(self):
        building = get_object_or_404(Building, slug=self.kwargs.get('slug'))
        return {
            'building': building,
        }

    # def get_success_url(self):
    #     return reverse_lazy('Building:building_photos', kwargs={'slug': self.object.slug})


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
