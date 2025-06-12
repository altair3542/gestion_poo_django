from django.urls import path
from . import views

urlpatterns = [
    path('ordenes/', views.OrdenListView.as_view(), name='orden_list'),
    path('ordenes/<int:pk>/', views.OrdenDetailView.as_view(), name='orden_detail'),
    path('ordenes/crear/', views.OrdenCreateView.as_view(), name='orden_create'),
    path('ordenes/<int:pk>/editar/', views.OrdenUpdateView.as_view(), name='orden_update'),
    path('ordenes/<int:pk>/eliminar/', views.OrdenDeleteView.as_view(), name='orden_delete'),
]
