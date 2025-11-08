Perfecto 💯 — estás entrando a la **segunda parte del proyecto “Parisina”**, ahora enfocada en el **modelo `Proveedor`**.
Te dejo **todo el procedimiento paso a paso**, con código completo, siguiendo el mismo estilo visual (colores Parisina: rojo, negro, amarillo, blanco).

---

## 🧱 **1. Migraciones**

En tu terminal de VS Code (dentro del entorno virtual activo):

```bash
python manage.py makemigrations
python manage.py migrate
```

Esto registra el modelo `Proveedor` en la base de datos.

---

## 📁 **2. Estructura de carpetas**

Dentro de `app_Parisina/templates/` crea la carpeta:

```
app_Parisina/
 ├─ templates/
 │   ├─ Cliente/
 │   ├─ Proveedor/    ← (nueva)
 │   │   ├─ agregar_proveedor.html
 │   │   ├─ ver_proveedor.html
 │   │   ├─ actualizar_proveedor.html
 │   │   └─ borrar_proveedor.html
 │   ├─ base.html
 │   ├─ navbar.html
 │   ├─ footer.html
 │   └─ inicio.html
```

---

## ⚙️ **3. Views.py** (CRUD completo del modelo `Proveedor`)

Agrega en `app_Parisina/views.py`:

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor

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
```

---

## 🌐 **4. urls.py de app_Parisina**

Crea (o edita) `app_Parisina/urls.py` y agrega las rutas CRUD para `Proveedor`:

```python
from django.urls import path
from . import views

urlpatterns = [
    # CLIENTE (ya existente)
    path('', views.inicio_parisina, name='inicio_parisina'),

    # PROVEEDOR
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('ver_proveedor/', views.ver_proveedor, name='ver_proveedor'),
    path('actualizar_proveedor/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('realizar_actualizacion_proveedor/<int:id>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('borrar_proveedor/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),
]
```

---

## ⚙️ **5. urls.py del proyecto backend_Parisina**

Abre `backend_Parisina/urls.py` y asegúrate de incluir las rutas de la app:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_Parisina.urls')),
]
```

---

## 🧩 **6. navbar.html actualizado**

En tu `templates/navbar.html`, actualiza la parte de **Proveedor**:

```html
<!-- PROVEEDOR -->
<li class="nav-item dropdown me-2">
  <a class="nav-link dropdown-toggle" href="#" id="proveedorMenu" data-bs-toggle="dropdown" aria-expanded="false">
    <i class="bi bi-truck"></i> Proveedor
  </a>
  <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="proveedorMenu">
    <li><a class="dropdown-item" href="{% url 'agregar_proveedor' %}">Agregar Proveedor</a></li>
    <li><a class="dropdown-item" href="{% url 'ver_proveedor' %}">Ver Proveedor</a></li>
  </ul>
</li>
```

---

## 🧱 **7. Templates CRUD (colores Parisina)**

### 🟥 `agregar_proveedor.html`

```html
{% extends 'base.html' %}
{% block content %}
<div class="card">
  <div class="card-header-accent">
    <h5>Agregar Proveedor</h5>
  </div>
  <div class="card-body">
    <form method="POST">
      {% csrf_token %}
      <div class="mb-3">
        <label>Nombre de la empresa</label>
        <input type="text" name="nombre_empresa" class="form-control" required>
      </div>
      <div class="mb-3">
        <label>Contacto</label>
        <input type="text" name="contacto" class="form-control" required>
      </div>
      <div class="mb-3">
        <label>Correo</label>
        <input type="email" name="correo" class="form-control" required>
      </div>
      <div class="mb-3">
        <label>Teléfono</label>
        <input type="text" name="telefono" class="form-control">
      </div>
      <div class="mb-3">
        <label>Dirección</label>
        <input type="text" name="direccion" class="form-control">
      </div>
      <div class="mb-3">
        <label>País</label>
        <input type="text" name="pais" class="form-control">
      </div>
      <button type="submit" class="btn btn-primary">Guardar</button>
      <a href="{% url 'ver_proveedor' %}" class="btn btn-outline-danger">Cancelar</a>
    </form>
  </div>
</div>
{% endblock %}
```

---

### 🟥 `ver_proveedor.html`

```html
{% extends 'base.html' %}
{% block content %}
<div class="card">
  <div class="card-header-accent">
    <h5>Lista de Proveedores</h5>
  </div>
  <div class="card-body">
    <table class="table table-hover align-middle">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre Empresa</th>
          <th>Contacto</th>
          <th>Correo</th>
          <th>Teléfono</th>
          <th>Dirección</th>
          <th>País</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        {% for proveedor in proveedores %}
        <tr>
          <td>{{ proveedor.id }}</td>
          <td>{{ proveedor.nombre_empresa }}</td>
          <td>{{ proveedor.contacto }}</td>
          <td>{{ proveedor.correo }}</td>
          <td>{{ proveedor.telefono }}</td>
          <td>{{ proveedor.direccion }}</td>
          <td>{{ proveedor.pais }}</td>
          <td>
            <a href="{% url 'actualizar_proveedor' proveedor.id %}" class="btn btn-sm btn-warning"><i class="bi bi-pencil"></i></a>
            <a href="{% url 'borrar_proveedor' proveedor.id %}" class="btn btn-sm btn-outline-danger"><i class="bi bi-trash"></i></a>
          </td>
        </tr>
        {% empty %}
        <tr><td colspan="8" class="text-center">No hay proveedores registrados.</td></tr>
        {% endfor %}
      </tbody>
    </table>
    <a href="{% url 'agregar_proveedor' %}" class="btn btn-primary">Agregar Proveedor</a>
  </div>
</div>
{% endblock %}
```

---

### 🟥 `actualizar_proveedor.html`

```html
{% extends 'base.html' %}
{% block content %}
<div class="card">
  <div class="card-header-accent">
    <h5>Actualizar Proveedor</h5>
  </div>
  <div class="card-body">
    <form method="POST" action="{% url 'realizar_actualizacion_proveedor' proveedor.id %}">
      {% csrf_token %}
      <div class="mb-3">
        <label>Nombre de la empresa</label>
        <input type="text" name="nombre_empresa" value="{{ proveedor.nombre_empresa }}" class="form-control">
      </div>
      <div class="mb-3">
        <label>Contacto</label>
        <input type="text" name="contacto" value="{{ proveedor.contacto }}" class="form-control">
      </div>
      <div class="mb-3">
        <label>Correo</label>
        <input type="email" name="correo" value="{{ proveedor.correo }}" class="form-control">
      </div>
      <div class="mb-3">
        <label>Teléfono</label>
        <input type="text" name="telefono" value="{{ proveedor.telefono }}" class="form-control">
      </div>
      <div class="mb-3">
        <label>Dirección</label>
        <input type="text" name="direccion" value="{{ proveedor.direccion }}" class="form-control">
      </div>
      <div class="mb-3">
        <label>País</label>
        <input type="text" name="pais" value="{{ proveedor.pais }}" class="form-control">
      </div>
      <button type="submit" class="btn btn-primary">Actualizar</button>
      <a href="{% url 'ver_proveedor' %}" class="btn btn-outline-danger">Cancelar</a>
    </form>
  </div>
</div>
{% endblock %}
```

---

### 🟥 `borrar_proveedor.html`

```html
{% extends 'base.html' %}
{% block content %}
<div class="card text-center">
  <div class="card-header-accent">
    <h5>Eliminar Proveedor</h5>
  </div>
  <div class="card-body">
    <p>¿Estás seguro que deseas eliminar al proveedor <strong>{{ proveedor.nombre_empresa }}</strong>?</p>
    <form method="POST">
      {% csrf_token %}
      <button type="submit" class="btn btn-outline-danger">Sí, eliminar</button>
      <a href="{% url 'ver_proveedor' %}" class="btn btn-warning">Cancelar</a>
    </form>
  </div>
</div>
{% endblock %}
```

---

## 🧾 **8. admin.py**

Registra el modelo `Proveedor`:

```python
from django.contrib import admin
from .models import Cliente, Proveedor

admin.site.register(Cliente)
admin.site.register(Proveedor)
```

Luego, realiza de nuevo:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🚀 **9. Ejecutar servidor**

Finalmente, ejecuta en el puerto **0559**:

```bash
python manage.py runserver 0559
```

Copia el enlace que aparece, por ejemplo:

```
http://127.0.0.1:0559/
```

y ábrelo en tu navegador.

---

¿Quieres que te deje la **tercera parte** ya preparada para el modelo `Producto` con la misma línea visual (rojo, negro, amarillo y blanco)?
Puedo generarte los `views.py`, `urls.py` y templates CRUD igual de bonitos y listos para pegar.

