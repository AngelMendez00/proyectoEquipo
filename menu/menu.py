from zoologico.zoologico import Zoologico
from empleados.empleado import Empleado
from director.director import Director
from visitantes.visitantes import Visitante
from datetime import date
from datetime import time
from datetime import datetime
from empleados.utils.rol import Rol
from animales.animal import Animal
from typing import List
from visitas.visita import Visita
from procesos.proceso import Proceso

class Menu:
    zoologico = Zoologico()
    
    def login(self, director: Director):
        intentos= 0
        while intentos < 3:
            print("Binvenido al Zoologico de Morelia")
            print("Inicia sesión para continuar")
            id_ingresada = input("Ingrese su ID: ")
            contraseña_ingresada= input("Ingrese su contraseña: ")
            if contraseña_ingresada == director.contraseña and id_ingresada== director.id:
                print("Inicio de sesión correcta")
                self.mostrar_menu()
            else:
                intentos = self.mostrar_intento_sesion_fallido(intentos_usuario=intentos)

        print("Máximos intentos de inicio de sesión alcanzados. Adiós")
        
    def mostrar_intento_sesion_fallido(self, intentos_usuario):
        print("\nContraseña incorrecta. Intenta de nuevo")
        return intentos_usuario + 1
    

    def mostrar_menu(self):
        while True:
            print("\n---BIENVENIDO---\n")
            print("Selecciona una opcion\n")
            print("1. Registrar empleado")
            print("2. Registrar visita")
            print("3. Registrar animal")
            print("4. Consultar empleados")
            print("5. Consultar visitantes")
            print("6. Registrar proceso")
            print("7. Salir")

            opcion=input("Opcion: ")

            
            if opcion == "1":
                print("\nSeleccionaste registrar empleado\n")
            
                registrar = 0 
                
                while registrar < 1 or registrar >= 5:
                    print("\nSelecciona el tipo de empleado a registrar\n")
                    print("1. Administrador")
                    print("2. Mantenimiento")
                    print("3. Veterinario")
                    print("4. Guia")
                    
                    registrar= int(input("Tipo de empleado a registrar: "))
                    
                    if registrar ==1:
                        rol=Rol.ADMINISTRACION
                    elif registrar == 2:
                        rol=Rol.MANTENIMIENTO
                    elif registrar == 3:
                        rol=Rol.VETERINARIO
                    elif registrar == 4:
                        rol=Rol.GUIA
                    else:
                        print("\nOpcion no valida vuelva a intentar\n")                   
               
                nombre=input("Ingresa el nombre: ")
                apellidos=input("Ingresa los apellidos: ")
                dia_nacimiento=int(input("Ingresa el dia de nacimiento: "))
                mes_nacimiento=int(input("Ingresa el mes de nacimiento: "))
                año_nacimiento=int(input("Ingresa el año de nacimiento: "))
                dia_inico=int(input("Ingresa el dia de inicio: "))
                mes_inicio=int(input("Ingresa el mes de inicio: "))
                año_incio=int(input("Ingresa el año de inicio: "))
                curp=input("Ingresa la curp: ")
                rfc=input("Ingresa RFC: ")
                salario=float(input("Ingresa el salario: "))
                horas_trabajo=int(input("Ingresa hora: "))
                minutos_trabajo=int(input("Ingresa minutos: "))

                fecha_nacimiento=date(año_nacimiento, mes_nacimiento, dia_nacimiento)
                fecha_inicio=date(año_incio, mes_inicio, dia_inico)
                horario=time(hour=horas_trabajo, minute=minutos_trabajo)

                

                empleado=Empleado(nombre=nombre,
                                        apellidos=apellidos,
                                        fecha_nacimiento=fecha_nacimiento,
                                        fecha_inicio=fecha_inicio,
                                        rfc=rfc,
                                        curp=curp,
                                        salario=salario,
                                        horario=horario,
                                        rol=rol)
                    
                self.zoologico.registrar_empleado(empleado=empleado)
            
            elif opcion == "2":
                visitantes=[]
                guia = None
                print("\nSelecionaste la opción de registrar visita")
                print("\nBoleto adulto: $100.00")
                print("\nBoleto niño: $50.00")
                
                if self.zoologico.mostrar_guia_disponibles() == True:
                 while guia == None:
                        id_guia = input("\nIngresa el ID del guia para esta visita: ")
                        guia = self.zoologico.validar_id_guia(id_guia=id_guia)
                else:
                    continue
                fecha_visita=date.today()

                cantidad_visitantes = int(input("\n¿Cuantos visitantes desea registrar?: "))
                
                while cantidad_visitantes > 0:

                    nuevo = input("\n¿Eres nuevo visitante? (S/N): ")
                    if nuevo == "S":
                        nombre=input("Ingresa el nombre: ")
                        apellidos=input("Ingresa los apellidos: ")
                        dia_nacimiento=int(input("Ingresa el dia de nacimiento: "))
                        mes_nacimiento=int(input("Ingresa el mes de nacimiento: "))
                        año_nacimiento=int(input("Ingresa el año de nacimiento: "))
                        curp=input("Ingresa la curp: ")
                        numero_visitas=0
                        fecha_registro=datetime.today()
                        fecha_nacimiento=date(año_nacimiento, mes_nacimiento, dia_nacimiento)
                        visitante=Visitante(nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento, curp=curp, numero_visitas=numero_visitas, fecha_registro=fecha_registro)
                        visitante.numero_visitas = visitante.numero_visitas + 1
                        self.zoologico.registrar_visitante(visitante=visitante)
                        
                        cantidad_visitantes = cantidad_visitantes - 1
                        visitantes.append(visitante)
                       
                    elif nuevo == "N":
                        visitante = None
                        while visitante == None:   
                            id = input("\n Ingresa tu ID: ")
                            visitante = self.zoologico.validar_id(id)
                            if visitante != None:   
                                cantidad_visitantes = cantidad_visitantes - 1
                                visitantes.append(visitante)
                                
                costo_total, adultos, niños = self.zoologico.revision_visitantes(visitantes=visitantes)
                
                print("\nPrecio total a pagar: ", costo_total)

                visita = Visita(guia_a_cargo=guia, costo_total=costo_total, visitantes=visitantes, fecha_visita=fecha_visita, cantidad_adultos=adultos,cantidad_niños=niños)
                
                self.zoologico.registrar_visita(visita=visita)

            elif opcion == "3":
                print("\nSeleccionaste registrar un animal\n")
                tipo = input("Ingresa el tipo/especie de animal: ")
                peso = float(input("Ingresa el peso en kg del animal: "))
                fecha_llegada = date.today()
                dia_nacimiento = int(input("Ingresa el dia de nacimiento del animal: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento del animal: "))
                año_nacimiento = int(input("Ingresa el año de nacimiento del animal: "))
                fecha_nacimiento = date(año_nacimiento, mes_nacimiento, dia_nacimiento)
                tipo_alimentacion = self.zoologico.capturar_tipo_alimentacion()
                frecuencia_alimentacion = input("Ingresa la frecuencia de alimentacion del animal: ")
                enfermedades = self.zoologico.capturar_enfermedades()
                vacunas = self.zoologico.capturar_vacunas()
                
                id = self.zoologico.generar_id_animal(tipo=tipo, fecha_llegada=fecha_llegada, fecha_nacimiento=fecha_nacimiento) 
    
                animal = Animal(id=id, tipo=tipo, fecha_llegada=fecha_llegada, enfermedades=enfermedades, tipo_alimentacion=tipo_alimentacion, fecha_nacimiento=fecha_nacimiento, peso=peso, frecuencia_alimentacion=frecuencia_alimentacion, vacunas=vacunas)
                self.zoologico.registrar_animal(animal=animal)
                self.zoologico.mostrar_animales()
 
            elif opcion == "4":
                print("\nSeleccionaste consultar empleado\n")
            
                consultar = 0 
                
                while consultar < 1 or consultar >= 5:
                    print("\nSelecciona el tipo de empleado a consultar\n")
                    print("1. Administrador")
                    print("2. Mantenimiento")
                    print("3. Veterinario")
                    print("4. Guia")
                
                    consultar= int(input("Tipo de empleado a consultar: "))

                    if consultar == 1:
                        self.zoologico.mostrar_administracion()
                    elif consultar == 2:
                        self.zoologico.mostrar_mantenimiento()
                    elif consultar == 3:
                        self.zoologico.mostrar_veterinarios()
                    elif consultar == 4:
                        self.zoologico.mostrar_guia()
                    else: 
                        print("Opcion no valida. Intente de nuevo")
            elif opcion == "5":
                self.zoologico.mostrar_visitantes()
                
            elif opcion == "6":
                print("*** Registrar proceso ***")
                
                tipo_proceso = self.zoologico.seleccion_tipo_proceso()
                self.zoologico.mostrar_mantenimiento_disponible()
                if self.zoologico.mostrar_mantenimiento_disponible() == True:
                    id_encargado = input("Ingresa el ID del empleado a encargarse: ")
                    empleado_encargado = self.zoologico.validar_id_encargado(id_encargado=id_encargado)
                    
                    while empleado_encargado == None:
                        print("No se ha podido registrar el guia, intenta de nuevo")
                        id_encargado = input("Ingresa el ID del empleado a encargarse: ")
                        empleado_encargado = self.zoologico.validar_id_encargado(id_encargado=id_encargado)
                else:
                    continue
                
                self.zoologico.mostrar_animales()
                if self.zoologico.mostrar_animales() == True:
                    id_animal = input("\nIngresa el ID del animal para realizar mantenimiento: ").upper()
                    id_animal = self.zoologico.validar_id_animal(id_animal=id_animal)
                    while id_animal == None:
                        print("No se ha podido registrar el animal, intenta de nuevo")
                        id_animal = input("\nIngresa el ID del animal para realizar mantenimiento: ").upper()
                        id_animal = self.zoologico.validar_id_animal(id_animal=id_animal)
                else:
                    continue
                
                observaciones = self.zoologico.observaciones()
                fecha_proceso = date.today()
                proceso = Proceso(empleado_encargado=empleado_encargado, tipo_proceso=tipo_proceso, observaciones=observaciones, fecha_proceso=fecha_proceso, id_animal=id_animal)
                self.zoologico.registrar_proceso(proceso=proceso)
  
            
            elif opcion == "7":
                print("\nAdios!!!\n")
                break
            else:
                print("\nOpcion no valida, intente de nuevo\n")