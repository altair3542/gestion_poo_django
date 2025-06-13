from django.core.exceptions import PermissionDenied

class TecnicoPropietarioMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.tecnico_asignado != request.user and not request.user.is_superuser:
            raise PermissionDenied('Usted que piensa de la vida, buscando lo que no debe ver.')
        return super().dispatch(request, *args, **kwargs)
