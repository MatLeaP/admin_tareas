from django.contrib import admin
from .models import Categoria, Operador, Tarea, Avatar

admin.site.register(Tarea)
admin.site.register(Operador)
admin.site.register(Categoria)
admin.site.register(Avatar)



