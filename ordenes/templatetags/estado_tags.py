from django import template

register = template.Library()

@register.filter
def formatear_estado(valor):
    colores = {
        'pendiente': '🟡 Pendiente',
        'en_progreso': '🔴 En Progreso',
        'finalizada': '🟢 Finalizada'
    }
    return colores.get(valor, valor)

@register.inclusion_tag('ordenes/components/tabla_ordenes.html')
def mostrar_tabla_ordenes(lista):
    return {'ordenes': lista}
