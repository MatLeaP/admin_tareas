from .models import Area, Categoria, Tarea, Avatar
from django.shortcuts import render, redirect
from django.contrib import  messages # el storage de messages esta definido en settings

# a trabajar las vistas por Clase:
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

# vistas para login y seguridad
# importo de FORMS el custom que realice de userregisterform y se lo envio a la vista con el data
from app_tareas.forms import CustomUserRegisterForm, AvatarFormulario, TareaForm, CategoriaForm, TareaEditForm, AreaForm
from django.contrib.auth.forms import AuthenticationForm
# funciones que me van a permitir autenticar al usuario
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
 
 
def home(request):
    return render(request, 'app_tareas/home.html') 

def about(request):
    return render(request, 'app_tareas/about/about.html')
         


## ------------ VISTAS REGISTRACION ---------------

def registro(request):
    data = {
        'form':CustomUserRegisterForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserRegisterForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro Correcto.")
            return redirect(to='home')
        
    return render(request, 'registration/registro.html', data)
    

class Logueo(LoginView):
    field = '__all__'
    redirect_authenticated_user: True
    
    def get_success_url(self):
        return reverse_lazy('home')
    
  
    
## ------------ VISTAS TAREAS ----------- 

class ListaTareas(LoginRequiredMixin, ListView):
    
    model = Tarea
    context_object_name = 'tareas'
    template_name = 'app_tareas/tareas/lista_tareas.html' 
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        # context['tareas'] = context['tareas'].filter(usuario=self.request.user) 
        #context['count'] = context['tareas'].filter(completo=False).count() 

        valor_buscado = self.request.GET.get('buscar') or ''
        if valor_buscado:
            context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscado)
        
        context['valor_buscado'] =  valor_buscado      
        return context


class DetalleTarea(LoginRequiredMixin,DetailView):
    
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'app_tareas/tareas/detalle_tarea.html'        
    
class CrearTarea(LoginRequiredMixin,CreateView):
    
    model = Tarea
    form_class = TareaForm
    success_url = reverse_lazy('tareas')
    template_name = 'app_tareas/tareas/form_tarea.html'
    
    def get_initial(self):
        data_inicial = super(CrearTarea, self).get_initial()
        data_inicial['usuario_carga'] = self.request.user
        return data_inicial
    
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.success(request, "Tarea Creada Correctamente.")
            return super(CrearTarea, self).post(request, **kwargs)  
    

class EditarTarea(LoginRequiredMixin,UpdateView):
    
    model = Tarea
    form_class = TareaEditForm
    success_url = reverse_lazy('tareas')
    template_name = 'app_tareas/tareas/form_tarea.html'  
    
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.success(request, "Tarea Editada Correctamente.")
            return super(EditarTarea, self).post(request, **kwargs)              
    
class EliminarTarea(LoginRequiredMixin,DeleteView):
    
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')   
    template_name = 'app_tareas/tareas/eliminar_tarea.html'  
    
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            messages.warning(request, "Tarea Eliminada Correctamente.")
            return super(EliminarTarea, self).post(request, **kwargs)            
        else:
            messages.error(request, "Error Al Eliminar Tarea.")          


def tarea(request, usuario_id):
    user = User.objects.filter(id = usuario_id)
    tareas = Tarea.objects.filter(usuario_id = user[0])
    return render(request, "app_tareas/tareas/tarea_usuario.html", {'tareas': tareas, 'usuario': user[0]})
 

# ---------- VISTAS CATEGORIAS -------------
 
class ListaCategorias(LoginRequiredMixin,ListView):
    
    model = Categoria
    context_object_name = 'categorias'   
    template_name = 'app_tareas/categorias/lista_categorias.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        valor_buscado = self.request.GET.get('buscar') or ''
        if valor_buscado:
            context['categorias'] = context['categorias'].filter(descripcion__icontains=valor_buscado)
        
        context['valor_buscado'] =  valor_buscado      
        return context    
         
    
class DetalleCategoria(LoginRequiredMixin,DetailView):
    
    model = Categoria
    context_object_name = 'categoria'
    template_name = 'app_tareas/categorias/detalle_categoria.html'       
    
class CrearCategoria(LoginRequiredMixin,CreateView):
    
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy('categorias')
    template_name = 'app_tareas/categorias/form_categoria.html'     

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.success(request, "Categoria Creada Correctamente.")
            return super(CrearCategoria, self).post(request, **kwargs)      

class EditarCategoria(LoginRequiredMixin,UpdateView):
    
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy('categorias')
    template_name = 'app_tareas/categorias/form_categoria.html'   
    
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.success(request, "Categoria Editada Correctamente.")
            return super(EditarCategoria, self).post(request, **kwargs)           
    
class EliminarCategoria(LoginRequiredMixin,DeleteView):
    
    model = Categoria
    context_object_name = 'categoria'
    success_url = reverse_lazy('categorias')      
    template_name = 'app_tareas/categorias/eliminar_categoria.html'   
    
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            messages.warning(request, "Categoria Eliminada Correctamente.")
            return super(EliminarCategoria, self).post(request, **kwargs)            
        else:
            messages.error(request, "Error Al Eliminar Categoria.") 



# ---------- VISTAS AREAS -------------
 
class ListaAreas(LoginRequiredMixin,ListView):
    
    model = Area
    context_object_name = 'areas'   
    template_name = 'app_tareas/areas/lista_areas.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        valor_buscado = self.request.GET.get('buscar') or ''
        if valor_buscado:
            context['areas'] = context['areas'].filter(descripcion__icontains=valor_buscado)
        
        context['valor_buscado'] =  valor_buscado      
        return context    
         
    
class DetalleArea(LoginRequiredMixin,DetailView):
    
    model = Area
    context_object_name = 'area'
    template_name = 'app_tareas/areas/detalle_area.html'       
    
class CrearArea(LoginRequiredMixin,CreateView):
    
    model = Area
    form_class = AreaForm
    success_url = reverse_lazy('areas')
    template_name = 'app_tareas/areas/form_area.html'     
    
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.success(request, "Area Creada Correctamente.")
            return super(CrearArea, self).post(request, **kwargs)      

class EditarArea(LoginRequiredMixin,UpdateView):
    
    model = Area
    form_class = AreaForm
    success_url = reverse_lazy('areas')
    template_name = 'app_tareas/areas/form_area.html'   
    
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.success(request, "Area Editada Correctamente.")
            return super(EditarArea, self).post(request, **kwargs)           
    
class EliminarArea(LoginRequiredMixin,DeleteView):
    
    model = Area
    context_object_name = 'area'
    success_url = reverse_lazy('areas')      
    template_name = 'app_tareas/areas/eliminar_area.html'   
    
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            messages.warning(request, "Area Eliminada Correctamente.")
            return super(EliminarArea, self).post(request, **kwargs)            
        else:
            messages.error(request, "Error Al Eliminar Area.") 
            
            

# ---------------- vista USERS ---------------
class ListaUsuarios(LoginRequiredMixin,ListView):
    
    model = User
    context_object_name = 'usuarios'   
    template_name = 'app_tareas/usuarios/lista_usuarios.html'       
    
    
class EditarUsuario(LoginRequiredMixin,UpdateView):
    
    model = User
    fields =  ['username','first_name', 'last_name', 'email'] 
    success_url = reverse_lazy('home')
    template_name = 'app_tareas/usuarios/form_usuario.html' 
 

def agregar_avatar(request):
    if request.method == 'POST':

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid:  
            avatar = form.save()
            avatar.user = request.user
            avatar.save()
            return redirect(reverse('home'))

    form = AvatarFormulario() 
    return render(request, "app_tareas/usuarios/form_avatar.html", {"form":form})


class EliminarAvatar(DeleteView):
    
    model = Avatar
    context_object_name = 'avatar'
    success_url = reverse_lazy('home')      
    template_name = 'app_tareas/categorias/eliminar_avatar.html' 
    
    
# --------------- CONTROL DE ERRORES -------------#

class Error404View(TemplateView):
    template_name = "app_tareas/error404.html"
    
   
    