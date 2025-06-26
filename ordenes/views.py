from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.shortcuts import redirect, render
from .models import OrdenServicio
from .mixins import TecnicoPropietarioMixin
from .forms import OrdenServicioForm, RegistroTecnicoForm
from django.contrib.auth.models import Group
from django.contrib.auth import login

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
    form_class = OrdenServicioForm
    template_name = 'ordenes/orden_form.html'
    success_url = reverse_lazy('orden_list')

    def form_valid(self, form):
        form.instance.tecnico_asignado = self.request.user
        return super().form_valid(form)


class OrdenUpdateView(LoginRequiredMixin, TecnicoPropietarioMixin, UpdateView):
    model = OrdenServicio
    form_class = OrdenServicioForm
    template_name = 'ordenes/orden_form.html'
    success_url = reverse_lazy('orden_list')


class OrdenDeleteView(LoginRequiredMixin, TecnicoPropietarioMixin, DeleteView):
    model = OrdenServicio
    template_name = 'ordenes/orden_confirm_delete.html'
    success_url = reverse_lazy('orden_list')

def ordenes_bulk_edit(request):
    OrdenFormSet = modelformset_factory(OrdenServicio, form=OrdenServicioForm, extra=0)
    queryset = OrdenServicio.objects.filter(tecnico_asignado=request.user)

    if request.method == 'POST':
        formset = OrdenFormSet(request.POST, queryset=queryset)
        if formset.is_valid():
            formset.save()
            return redirect('orden_list')
    else:
        formset = OrdenFormSet(queryset=queryset)

    return render(request, 'ordenes/orden_formset.html', {'formset': formset})

def registrar_tecnico(request):
    if request.method == 'POST':
        form = RegistroTecnicoForm(request.POST)
        if form.is_valid():
            user = form.save()
            perfil = user.perfilusuario
            perfil.cargo = form.cleaned_data['cargo']
            perfil.especialidad = form.cleaned_data['especialidad']
            perfil.save()

            grupo, creado = Group.objects.get_or_create(name=perfil.cargo)
            user.groups.add(grupo)

            login(request, user)
            return redirect('orden_list')
    else:
        form = RegistroTecnicoForm()
    return render(request, 'ordenes/registro_tecnico.html', {'form': form})
