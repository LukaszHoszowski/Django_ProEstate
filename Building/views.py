from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from Building.forms import BuildingPhotosForm, BuildingDocsForm, FlatUpdateForm
from Building.models import Building, Flat


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


class BuildingFlatsView(LoginRequiredMixin, DetailView):
    model = Building
    context_object_name = 'building'
    template_name = 'Building/building_flats.html'
    ordering = ['flat.number']
    slug_field = 'slug'


class FlatDetailView(LoginRequiredMixin, DetailView):
    model = Flat
    context_object_name = 'flat'
    template_name = 'Building/flat_details.html'


class FlatUpdateView(LoginRequiredMixin, UpdateView):
    model = Flat
    form_class = FlatUpdateForm
    context_object_name = 'flat'
    template_name = 'Building/flat_update.html'
    # success_url = reverse_lazy('Building:flat_details', )

    def get_success_url(self):
        return reverse_lazy('Building:flat_details', kwargs={'slug': self.object.building.slug, 'pk': self.object.pk})


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


class BuildingDocsView(LoginRequiredMixin, DetailView):
    model = Building
    context_object_name = 'building'
    paginate_by = 8
    template_name = 'Building/building_documents.html'
    slug_field = 'slug'


class BuildingDocsCreate(LoginRequiredMixin, CreateView):
    form_class = BuildingDocsForm
    template_name = 'Building/building_documents_create.html'

    def form_valid(self, form):
        form.instance.piece = Building.objects.get(slug=self.kwargs['slug'])
        return super(BuildingDocsCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('Building:building_documents', kwargs={'slug': self.kwargs['slug']})

    def get_initial(self):
        building = get_object_or_404(Building, slug=self.kwargs.get('slug'))
        return {
            'building': building,
        }


class BuildingPhotosView(LoginRequiredMixin, DetailView):
    model = Building
    context_object_name = 'building'
    paginate_by = 8
    template_name = 'Building/building_photos.html'
    slug_field = 'slug'


class BuildingPhotosCreate(LoginRequiredMixin, CreateView):
    form_class = BuildingPhotosForm
    template_name = 'Building/building_photos_create.html'

    def form_valid(self, form):
        form.instance.piece = Building.objects.get(slug=self.kwargs['slug'])
        return super(BuildingPhotosCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('Building:building_photos', kwargs={'slug': self.kwargs['slug']})

    def get_initial(self):
        building = get_object_or_404(Building, slug=self.kwargs.get('slug'))
        return {
            'building': building,
        }
