from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import OrdenServicio
from .mixins import TecnicoPropietarioMixin

# Create your views here.

class OrdenListView(LoginRequiredMixin, ListView):
    model = OrdenServicio
    context_object_name = 'ordenes'
    template_name = 'ordenes/orden_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return OrdenServicio.objects.all()
        return OrdenServicio.objects.filter(tecnico_asignado=self.request.user)

class OrdenDetailView(LoginRequiredMixin, DetailView):
    model = OrdenServicio
    template_name = 'ordenes/orden_detail.html'

class OrdenCreateView(LoginRequiredMixin, CreateView):
    model = OrdenServicio
    fields = ['descripcion', 'estado']
    template_name = 'ordenes/orden_form.html'
    success_url = reverse_lazy('orden_list')

    def form_valid(self, form):
        form.instance.tecnico_asignado = self.request.user
        return super().form_valid(form)
class OrdenUpdateView(LoginRequiredMixin, TecnicoPropietarioMixin, UpdateView):
    model = OrdenServicio
    fields = ['descripcion', 'estado']
    template_name = 'ordenes/orden_form.html'
    success_url = reverse_lazy('orden_list')


class OrdenDeleteView(LoginRequiredMixin, TecnicoPropietarioMixin, DeleteView):
    model = OrdenServicio
    template_name = 'ordenes/orden_confirm_delete.html'
    success_url = reverse_lazy('orden_list')
