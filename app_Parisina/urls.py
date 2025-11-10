from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio_parisina, name="inicio_parisina"),
    path("cliente/agregar/", views.agregar_cliente, name="agregar_cliente"),
    path("cliente/ver/", views.ver_cliente, name="ver_cliente"),
    path("cliente/actualizar/<int:pk>/", views.actualizar_cliente, name="actualizar_cliente"),
    path("cliente/realizar_actualizacion/<int:pk>/", views.realizar_actualizacion_cliente, name="realizar_actualizacion_cliente"),
    path("cliente/borrar/<int:pk>/", views.borrar_cliente, name="borrar_cliente"),

    # PROVEEDOR
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('ver_proveedor/', views.ver_proveedor, name='ver_proveedor'),
    path('actualizar_proveedor/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('realizar_actualizacion_proveedor/<int:id>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('borrar_proveedor/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),
]