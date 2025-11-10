from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .models import Proveedor

# Página inicio del sistema
def inicio_parisina(request):
    return render(request, "inicio.html")

# Agregar cliente (muestra formulario y procesa POST)
def agregar_cliente(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        apellido = request.POST.get("apellido", "").strip()
        correo = request.POST.get("correo_electronico", "").strip()
        telefono = request.POST.get("telefono", "").strip()
        direccion = request.POST.get("direccion", "").strip()
        ciudad = request.POST.get("ciudad", "").strip()

        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            correo_electronico=correo,
            telefono=telefono,
            direccion=direccion,
            ciudad=ciudad
        )
        return redirect("ver_cliente")
    return render(request, "Cliente/agregar_Cliente.html")

# Ver clientes (lista en tabla)
def ver_cliente(request):
    clientes = Cliente.objects.all().order_by("-fecha_registro")
    return render(request, "Cliente/ver_Cliente.html", {"clientes": clientes})

# Mostrar formulario para actualizar cliente
def actualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, "Cliente/actualizar_Cliente.html", {"cliente": cliente})

# Procesar la actualización (acción POST)
def realizar_actualizacion_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.nombre = request.POST.get("nombre", cliente.nombre)
        cliente.apellido = request.POST.get("apellido", cliente.apellido)
        cliente.correo_electronico = request.POST.get("correo_electronico", cliente.correo_electronico)
        cliente.telefono = request.POST.get("telefono", cliente.telefono)
        cliente.direccion = request.POST.get("direccion", cliente.direccion)
        cliente.ciudad = request.POST.get("ciudad", cliente.ciudad)
        cliente.save()
        return redirect("ver_cliente")
    # si no es POST, redirigir a formulario
    return redirect("actualizar_cliente", pk=pk)

# Borrar cliente (confirmación GET y eliminación POST)
def borrar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect("ver_cliente")
    return render(request, "Cliente/borrar_Cliente.html", {"cliente": cliente})


# =========================
# AGREGAR PROVEEDOR
# =========================
def agregar_proveedor(request):
    if request.method == 'POST':
        nombre_empresa = request.POST.get('nombre_empresa')
        contacto = request.POST.get('contacto')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        pais = request.POST.get('pais')

        Proveedor.objects.create(
            nombre_empresa=nombre_empresa,
            contacto=contacto,
            correo=correo,
            telefono=telefono,
            direccion=direccion,
            pais=pais
        )
        return redirect('ver_proveedor')
    return render(request, 'Proveedor/agregar_proveedor.html')


# =========================
# VER PROVEEDORES
# =========================
def ver_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'Proveedor/ver_proveedor.html', {'proveedores': proveedores})


# =========================
# ACTUALIZAR PROVEEDOR
# =========================
def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    return render(request, 'Proveedor/actualizar_proveedor.html', {'proveedor': proveedor})


# =========================
# REALIZAR ACTUALIZACIÓN
# =========================
def realizar_actualizacion_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.nombre_empresa = request.POST.get('nombre_empresa')
        proveedor.contacto = request.POST.get('contacto')
        proveedor.correo = request.POST.get('correo')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.pais = request.POST.get('pais')
        proveedor.save()
        return redirect('ver_proveedor')
    return render(request, 'Proveedor/actualizar_proveedor.html', {'proveedor': proveedor})


# =========================
# BORRAR PROVEEDOR
# =========================
def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedor')
    return render(request, 'Proveedor/borrar_proveedor.html', {'proveedor': proveedor})