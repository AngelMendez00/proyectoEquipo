from empleados.empleado import Empleado
from visitantes.visitantes import Vistante
from usuarios.usuario import Usuario
from typing import List
from datetime import time
from datetime import date
from empleados.utils.rol import Rol
from animales.animal import Animal

class Zoologico:
    lista_empleados:List[Empleado]=[]
    lista_usuario: List[Usuario]=[]
    lista_visitantes: List[Vistante]=[Vistante]
    lista_animales: List[Animal]=[Animal]
    
    

    def __init__(self):
        director=Empleado("Juan", "Gonzalez", date(2003, 10, 16), date(2020, 12, 12), "JUANO777", "JUSP20031016", 2000.00, time(8,30), Rol.DIRECTOR)
        self.lista_empleados.append(director)

    def registrar_visitante(self, visitante: Vistante):
        self.lista_visitantes.append(visitante)
        self.lista_usuario.append(visitante)

    def registrar_empleado(self, empleado: Empleado):
        self.lista_empleados.append(empleado)
        self.lista_usuario.append(empleado)
    
    def registrar_animal(self, animal: Animal):
        self.lista_animales.append(animal)
        
    def mostrar_animales(self):
        print("*** ANIMALES EN EL ZOOLOGICO ***")
        for animal in self.lista_animales: 
            print(animal.mostrar_info_animal())
            
        




            