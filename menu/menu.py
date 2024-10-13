from zoologico.zoologico import Zoologico
from empleados.empleado import Empleado
from usuarios.usuario import Usuario
from datetime import date
from datetime import time
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
            print("4. Salir")

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
            
            
            elif opcion == "3":
                print("\nSeleccionaste registrar un animal\n")
                tipo = input("Ingresa el tipo/especie de animal: ")
                peso = float(input("Ingresa el peso en kg del animal: "))
                fecha_llegada = date.today()
                dia_nacimiento = int(input("Ingresa el dia de nacimiento del animal: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento del animal: "))
                año_nacimiento = int(input("Ingresa el año de nacimiento del animal: "))
                fecha_nacimiento = date(año_nacimiento, mes_nacimiento, dia_nacimiento)
                
                
                tipo_alimentacion = 0
                
                while tipo_alimentacion <1 or tipo_alimentacion >=4:
                    tipo_alimentacion = int(input("Ingresa el tipo de alimentacion del animal: \n1. Herviboro \n2. Carnivoro \n3. Omnivoro"))
                    if tipo_alimentacion == 1:
                        tipo_alimentacion = Alimentacion.HERVIBORO
                    elif tipo_alimentacion == 2:
                        tipo_alimentacion = Alimentacion.CARNIVORO
                    elif tipo_alimentacion == 3:
                        tipo_alimentacion = Alimentacion.OMNIVORO
                    else:
                        print("Opcion invalida. Intenta de nuevo")
                        
                frecuencia_alimentacion = input("Ingresa la frecuencia de alimentacion del animal: ")
                
                enfermedades = []
                enfermedad=0
                while enfermedad <1 or enfermedad >=3:
                    cuenta_con_enfermedad = int(input("Ingresa si el animal cuenta con enfermedades: \n1. Si \n2. No \n: "))
                    if cuenta_con_enfermedad == 1:
                        opcion_enfermedad = 0
                        while opcion_enfermedad != 2:
                            opcion_enfermedad = int(input("1. Agregar enfermedad \n2.Terminar "))
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
                id = animal.generar_id_animal(tipo=tipo, fecha_llegada=fecha_llegada, año_nacimiento=año_nacimiento)     
                animal = Animal(id=id, tipo=tipo, fecha_llegada=fecha_llegada, enfermedades=enfermedades, tipo_alimentacion=tipo_alimentacion, fecha_nacimiento=fecha_nacimiento, peso=peso, frecuencia_alimentacion=frecuencia_alimentacion, vacunas=vacunas)
                self.zoologico.registrar_animal(animal=animal)
 
    
            elif opcion == "4":
                print("\nAdios!!!\n")
                break
            else:
                print("\nOpcion no valida, intente de nuevo\n")