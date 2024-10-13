from empleados.empleado import Empleado
from visitantes.visitantes import Visitante
from usuarios.usuario import Usuario
from typing import List
from datetime import datetime
from datetime import time
from datetime import date
from empleados.utils.rol import Rol
from animales.animal import Animal
from random import randint

class Zoologico:
    lista_empleados:List[Empleado]=[]
    lista_usuario: List[Usuario]=[]
    lista_visitantes: List[Visitante]=[]
    lista_animales: List[Animal]=[]

    def __init__(self):
        director=Empleado("Juan", "Gonzalez", date(2003, 10, 16), date(2020, 12, 12), "JUANO777", "JUSP20031016", 2000.00, time(8,30), Rol.DIRECTOR)
        self.lista_empleados.append(director)

    def registrar_visitante(self, visitante: Visitante):
        self.lista_visitantes.append(visitante)
        self.lista_usuario.append(visitante)

    def registrar_empleado(self, empleado: Empleado):
        self.lista_empleados.append(empleado)
        self.lista_usuario.append(empleado)
    
    def registrar_animal(self, animal: Animal):
        self.lista_animales.append(animal)
        
    def mostrar_animales(self):
        print("\n*** ANIMALES EN EL ZOOLOGICO ***")
        for animal in self.lista_animales: 
            print(animal.mostrar_info_animal())
    
    def generar_id_animal(self, tipo, fecha_llegada, fecha_nacimiento):
        id = f"AN{tipo[:2].upper()}{str(fecha_llegada.year)[-2:]}{str(fecha_llegada.month)}{randint(1, 10000)}{datetime.now().day}{str(fecha_nacimiento.year)[-2:]}"
        return id
            
    def mostrar_veterinarios(self):
        print("\n---VETERINARIOS---\n")
        for empleado in self.lista_empleados:
            if empleado.rol == Rol.VETERINARIO:
                print(empleado.mostrar_info())
    
    def mostrar_administracion(self):
        print("\n---ADMINISTRADORES---\n")
        for empleado in self.lista_empleados:
            if empleado.rol == Rol.ADMINISTRACION:
                print(empleado.mostrar_info())
    
    def mostrar_mantenimiento(self):
        print("\n---ENCARGADOS DE MANTENIMIENTO---\n")
        for empleado in self.lista_empleados:
            if empleado.rol == Rol.MANTENIMIENTO:
                print(empleado.mostrar_info())
    
    def mostrar_guia(self):
        print("\n---GUIAS---\n")
        for empleado in self.lista_empleados:
            if empleado.rol == Rol.GUIA:
                print(empleado.mostrar_info())

    def mostrar_visitantes(self):
        print("\n---VISITANTES---\n")
        for visitantes in self.lista_visitantes:
            print(visitantes.mostrar_info_visitante())

    


            