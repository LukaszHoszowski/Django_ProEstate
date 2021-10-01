from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from Building.forms import BuildingPhotosForm, BuildingDocsForm, FlatUpdateForm, MeasureUpdateForm
from Building.models import Building, Flat, Measure


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
        form.instance.building = Building.objects.get(slug=self.kwargs['slug'])
        return super(BuildingDocsCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('Building:building_documents', kwargs={'slug': self.kwargs['slug']})


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
        form.instance.building = Building.objects.get(slug=self.kwargs['slug'])
        return super(BuildingPhotosCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('Building:building_photos', kwargs={'slug': self.kwargs['slug']})


class FlatDetailView(LoginRequiredMixin, DetailView):
    model = Flat
    context_object_name = 'flat'
    template_name = 'Building/flat_details.html'


class FlatUpdateView(LoginRequiredMixin, UpdateView):
    model = Flat
    form_class = FlatUpdateForm
    context_object_name = 'flat'
    template_name = 'Building/flat_update.html'

    def get_success_url(self):
        return reverse_lazy('Building:flat_details', kwargs={'slug': self.object.building.slug, 'pk': self.object.pk})


class FlatAddUserUpdate(LoginRequiredMixin, View):
    def post(self, request, pk):
        flat = Flat.objects.get(pk=pk)
        flat.user.add(request.user)
        flat.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class FlatDeleteUserUpdate(LoginRequiredMixin, View):
    def post(self, request, pk):
        flat = Flat.objects.get(pk=pk)
        flat.user.remove(request.user)
        flat.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class MeasureUpdateView(LoginRequiredMixin, UpdateView):
    model = Measure
    form_class = MeasureUpdateForm
    context_object_name = 'measure'
    template_name = 'Building/measure_update.html'

    def get_success_url(self):
        return reverse_lazy('Building:flat_details',
                            kwargs={'slug': self.object.flat.building.slug, 'pk': self.object.flat.pk})
