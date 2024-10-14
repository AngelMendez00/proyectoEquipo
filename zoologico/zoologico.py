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
from procesos.proceso import Proceso
from procesos.utils.tipos_procesos import TiposProcesos

class Zoologico:
    lista_empleados:List[Empleado]=[]
    lista_usuario: List[Usuario]=[]
    lista_animales: List[Animal]=[]
    lista_visitantes: List[Visitante]=[]
    lista_visitas: List[Visita]=[]
    lista_procesos: List[Proceso]=[]

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
    
    def registrar_proceso(self, proceso: Proceso):
        self.lista_procesos.append(proceso)
    
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
            cantidad_animales =+ 1
        if cantidad_animales == 0:
            print("NO HAY ANIMALES A MOSTRAR")
            return False
        else:
            return True
    
    def generar_id_animal(self, tipo, fecha_llegada, fecha_nacimiento):
        id = f"AN{tipo[:2].upper()}{str(fecha_llegada.year)[-2:]}{str(fecha_llegada.month)}{randint(1, 10000)}{datetime.now().day}{str(fecha_nacimiento.year)[-2:]}"
        return id
    
    def mostrar_procesos(self):    
        print("\n--- Procesos realizados ---")
        for proceso in self.lista_procesos:
            print(proceso.mostrar_info_proceso())
           
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
                
    def mostrar_mantenimiento_disponible(self):
        print("\n---ENCARGADOS DE MANTENIMIENTO DISPONIBLES---\n")
        numero_disponibles = 0
        for empleado in self.lista_empleados:
            if empleado.rol == Rol.MANTENIMIENTO:
                if empleado.disponible == True:
                    print(empleado.mostrar_info())
                    numero_disponibles =+ 1
        if numero_disponibles == 0:
            print("NO HAY EMPLEADOS DE MANTENIMIENTO DISPONIBLES")
            return False
        else:
            return True
    
    def mostrar_guia(self):
        print("\n---GUIAS---\n")
        for empleado in self.lista_empleados:
            if empleado.rol == Rol.GUIA:
                print(empleado.mostrar_info())

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

    def mostrar_visitantes(self):
        print("\n---VISITANTES---\n")
        for visitantes in self.lista_visitantes:
            print(visitantes.mostrar_info_visitante())
    
    def registrar_visita(self, visita: Visita):
        self.lista_visitas.append(visita)

    def revision_visitantes(self, visitantes:List[Visitante]=[]):
        precio = 0
        adultos= 0
        niños = 0
        for visitante in visitantes:
            if (datetime.now().year - visitante.fecha_nacimiento.year) < 18:
                niños=+1
                if visitante.numero_visitas == 6:
                    precio = precio + (50 * 0.8)
                    visitante.numero_visitas = 0
                else:
                    precio = precio + 50
            else:
                adultos=+1
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
                
    def validar_id_animal(self, id_animal:str):
        for animal in self.lista_animales:
            if id_animal == animal.id:
               return id_animal
        else:
            print("El ID es incorrecto") 
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
        
    def validar_id_encargado(self, id_encargado:str):
        for empleado in self.lista_empleados:
            if id_encargado == empleado.id:
                if empleado.rol == Rol.MANTENIMIENTO:
                    empleado.disponible = False
                    return empleado
                else: 
                    print("El empleado no es de mantenimiento")
         
        print("ID no encontrada")
        return None

    def seleccion_tipo_proceso(self):
        opcion_proceso = 0
                
        while opcion_proceso <1 or opcion_proceso >= 4:
            
            print("1. Mantenimiento")
            print("2. Alimentacion")
            print("3. Limpieza")
            opcion_proceso = int(input("Selecciona el tipo de proceso a registrar: "))
            
            if opcion_proceso == 1:
                tipo_proceso = TiposProcesos.MANTENIMIENTO
                return tipo_proceso
            elif opcion_proceso == 2:
                tipo_proceso = TiposProcesos.ALIMENTACION
                return tipo_proceso
            elif opcion_proceso == 3:
                tipo_proceso = TiposProcesos.LIMPIEZA
                return tipo_proceso
            else:
                print("Opcion invalida. Intenta de nuevo")
    
    def observaciones(self):           
                    
        registrar_observaciones = 0
        while registrar_observaciones !=2 :    
            print("Desea ingresar observaciones?")
            print("\n1. Si \n2. No")
            registrar_observaciones = int(input(": "))
            if registrar_observaciones == 1:
                observaciones = input("Escribe tus observaciones: ")
                return observaciones
            elif registrar_observaciones == 2:
                observaciones = None
                return observaciones
            else:
                print("Opcion no valida")



            