from django.test import TestCase

# Create your tests here.
from random import randint, choice
import random 
import datetime
import string
from .models import Tarea,Categoria
from django.contrib.auth.models import User



class CategoriaTestCase(TestCase):
    pass

    def test_creacion_categoria(self):
        
        descripcion = "Trabajos"

        descripcion_prueba = descripcion

        categoria_1= Categoria(descripcion= descripcion_prueba)
        print(descripcion)

        self.assertEqual(categoria_1.descripcion, descripcion_prueba)
        

    def test_creacion_categoria_cien(self):
            palabras = [random.choice(string.ascii_letters + string.digits) for _ in range(199)]
            descripcion = "".join(palabras)
            
            descripcion_prueba = descripcion

            categoria_1= Categoria(descripcion= descripcion_prueba)
            print(descripcion)
            
            self.assertEqual(categoria_1.descripcion, descripcion_prueba)

    def test_creacion_categoria_doscientos(self):
            palabras = [random.choice(string.ascii_letters + string.digits) for _ in range(201)]
            descripcion = "".join(palabras)
            
            descripcion_prueba = descripcion

            categoria_1= Categoria(descripcion= descripcion_prueba)
            print(descripcion)
            
            self.assertEqual(categoria_1.descripcion, descripcion_prueba)