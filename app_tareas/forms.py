from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from app_tareas.models import Avatar, Categoria, Tarea

class CustomUserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario')
    first_name = forms.CharField(max_length=150,label='Nombre')
    last_name = forms.CharField(max_length=150,label='Apellido')
    email = forms.CharField(max_length=150,label='Email')
    password1 = forms.CharField(label='Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget = forms.PasswordInput)
    
    # # class meta, es como una uperclase que tiene la clase dentro
    class Meta:
         model = User
         fields = ['username','last_name', 'first_name',  'email', 'password1', 'password2']
        
class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']
        
        
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['usuario','titulo','descripcion', 'categoria']        

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion']        

 
