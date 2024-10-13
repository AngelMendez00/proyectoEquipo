from zoologico.zoologico import Zoologico
from empleados.empleado import Empleado
from visitantes.visitantes import Visitante
from usuarios.usuario import Usuario
from datetime import date
from datetime import time
from datetime import datetime
from empleados.utils.rol import Rol
from animales.animal import Animal
from typing import List
from animales.utils.alimentacion import Alimentacion

class Menu:
    zoologico = Zoologico()
    
    def mostrar_menu(self):
        while True:
            print("\n---BIENVENIDO---\n")
            print("Selecciona una opcion\n")
            print("1. Registrar empleado")
            print("2. Registrar visitante")
            print("3. Registrar animal")
            print("4. Consultar empleados")
            print("5. Consultar visitantes")
            print("6. Salir")

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
                print("\nSeleccionaste registrar visitante\n")

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
                
                self.zoologico.registrar_visitante(visitante=visitante) 

            elif opcion == "3":
                print("\nSeleccionaste registrar un animal\n")
                tipo = input("Ingresa el tipo/especie de animal: ")
                peso = float(input("Ingresa el peso en kg del animal: "))
                fecha_llegada = date.today()
                dia_nacimiento = int(input("Ingresa el dia de nacimiento del animal: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento del animal: "))
                año_nacimiento = int(input("Ingresa el año de nacimiento del animal: "))
                fecha_nacimiento = date(año_nacimiento, mes_nacimiento, dia_nacimiento)
                
                
                ciclo_alimentacion = 0
                while ciclo_alimentacion < 1 or ciclo_alimentacion >= 4:
                    ciclo_alimentacion = int(input("Ingresa el tipo de alimentacion del animal: \n1. Herviboro \n2. Carnivoro \n3. Omnivoro \n: "))
                    
                    if ciclo_alimentacion == 1:
                        tipo_alimentacion = Alimentacion.HERVIBORO
                    elif ciclo_alimentacion == 2:
                        tipo_alimentacion = Alimentacion.CARNIVORO
                    elif tipo_alimentacion == 3:
                        ciclo_alimentacion = Alimentacion.OMNIVORO
                    else:
                        print("Opcion invalida. Intenta de nuevo")
                        
                frecuencia_alimentacion = input("Ingresa la frecuencia de alimentacion del animal: ")
                
                enfermedades = []
                opcion_enfermedad = 0
                while opcion_enfermedad <1 or opcion_enfermedad >=3:
                    cuenta_con_enfermedad = int(input("Ingresa si el animal cuenta con enfermedades: \n1. Si \n2. No \n: "))
                    if cuenta_con_enfermedad == 1:
                        opcion_enfermedad = 0
                        enfermedad = input("Ingresa la enfermedad del animal: ")
                        enfermedades.append(enfermedad)
                        while opcion_enfermedad != 2:
                            opcion_enfermedad = int(input("1. Agregar enfermedad \n2.Terminar \n: "))
                            if opcion_enfermedad == 1:
                                enfermedad = input("Ingresa la enfermedad del animal: ")
                                enfermedades.append(enfermedad)
                            elif opcion_enfermedad != 2: 
                                print("Opcion invalida. Intenta de nuevo")
                                
                    elif cuenta_con_enfermedad == 2:
                        break
                    else:
                        print("Opcion invalida. Intenta de nuevo")   
                        
                vacunado = 0
                while vacunado <1 or vacunado >=3:
                    vacunado = int(input("El animal esta vacunado? \n1. Si \n2. No \n: " ))
                    if vacunado == 1:
                        vacunas = True
                    elif vacunado == 2:
                        vacunas = False
                    else:
                        print("Opción inválida. Intenta de nuevo.")
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
            elif opcion == "5":
                self.zoologico.mostrar_visitantes()
            elif opcion == "6":
                print("\nAdios!!!\n")
                break
            else:
                print("\nOpcion no valida, intente de nuevo\n")