from empleados.empleado import Empleado
from visitantes.visitantes import Visitante
from visitas.visita import Visita
from usuarios.usuario import Usuario
from typing import List
from datetime import datetime
from datetime import time
from datetime import date
from empleados.utils.rol import Rol
from animales.animal import Animal
from random import randint
from animales.utils.alimentacion import Alimentacion

class Zoologico:
    lista_empleados:List[Empleado]=[]
    lista_usuario: List[Usuario]=[]
    lista_animales: List[Animal]=[]
    lista_visitantes: List[Visitante]=[]
    lista_visitas: List[Visita]=[]
    

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
     
    def capturar_tipo_alimentacion(self):   
        ciclo_alimentacion = 0
        while ciclo_alimentacion < 1 or ciclo_alimentacion >= 4:
            ciclo_alimentacion = int(input("Ingresa el tipo de alimentacion del animal: \n1. Herviboro \n2. Carnivoro \n3. Omnivoro \n: "))
            
            if ciclo_alimentacion == 1:
                tipo_alimentacion = Alimentacion.HERVIBORO
                return tipo_alimentacion
            elif ciclo_alimentacion == 2:
                tipo_alimentacion = Alimentacion.CARNIVORO
                return tipo_alimentacion
            elif ciclo_alimentacion == 3:
                tipo_alimentacion = Alimentacion.OMNIVORO
                return tipo_alimentacion
            else:
                print("Opcion invalida. Intenta de nuevo")
                
    def capturar_enfermedades(self):
        opcion_enfermedad = 0
        enfermedades = []
        while opcion_enfermedad <1 or opcion_enfermedad >=3:
            cuenta_con_enfermedad = int(input("Ingresa si el animal cuenta con enfermedades: \n1. Si \n2. No \n: "))
            if cuenta_con_enfermedad == 1:
                opcion_enfermedad = 0
                enfermedad = input("Ingresa la enfermedad del animal: ")
                enfermedades.append(enfermedad)
                while opcion_enfermedad != 2:
                    opcion_enfermedad = int(input("Agregar otra enfermedad. \n1. Si \n2. No \n: "))
                    if opcion_enfermedad == 1:
                        enfermedad = input("Ingresa la enfermedad del animal: ")
                        enfermedades.append(enfermedad)
                    elif opcion_enfermedad != 2: 
                        print("Opcion invalida. Intenta de nuevo")
                        
            elif cuenta_con_enfermedad == 2:
                break
            else:
                print("Opcion invalida. Intenta de nuevo")   
        if len(enfermedades) == 0:
            enfermedad = "Sin enfermedades"
            enfermedades.append(enfermedad)
            return enfermedades
        else:
            return enfermedades  
              
    def capturar_vacunas(self):  
        vacunado = 0
        while vacunado <1 or vacunado >=3:
            vacunado = int(input("El animal esta vacunado? \n1. Si \n2. No \n: " ))
            if vacunado == 1:
                vacunas = True
            elif vacunado == 2:
                vacunas = False
            else:
                print("Opción inválida. Intenta de nuevo.")       
        return vacunas           
    
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

    def mostrar_guia_disponibles(self):
        disponibilidad = 0
        print("\n---GUIAS DISPONIBLES---\n")
        for empleado in self.lista_empleados:
            if empleado.rol == Rol.GUIA:
                if empleado.disponible == True:
                    print(empleado.mostrar_info())
                    disponibilidad =+ 1
        if disponibilidad == 0:
            print("\nNO HAY GUIAS DISPONIBLES\n")
            return False
        else:
            return True
        

    def registrar_visita(self, visita: Visita):
        self.lista_visitas.append(visita)

    def revision_visitantes(self, visitantes:List[Visitante]=[]):
        precio = 0
        adultos= 0
        niños = 0
        for visitante in visitantes:
            if (datetime.now().year - visitante.fecha_nacimiento.year) < 18:
                niños+1
                if visitante.numero_visitas == 6:
                    precio = precio + (50 * 0.8)
                    visitante.numero_visitas = 0
                else:
                    precio = precio + 50
            else:
                adultos+1
                if visitante.numero_visitas == 6:
                    precio = precio + (100 * 0.8)
                    visitante.numero_visitas = 0
                else:
                    precio = precio + 100

        return precio, adultos, niños
                    
    def validar_id(self, id:str):
        for visitante in self.lista_visitantes:
            if id == visitante.id:
                visitante.numero_visitas = visitante.numero_visitas + 1
                return visitante
        print("\nID no encontrada")
        return None

    def validar_id_guia(self, id_guia:str):
        for empleado in self.lista_empleados:
            if id_guia == empleado.id:
                if empleado.rol == Rol.GUIA:
                    if empleado.disponible == True:
                        empleado.disponible = False
                        return empleado
        print("\nID no encontrada o guia no disponible")
        print("Vuelva a intentarlo")
        return None

         
        






            