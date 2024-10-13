from zoologico.zoologico import Zoologico
from empleados.empleado import Empleado
from usuarios.usuario import Usuario
from datetime import date
from datetime import time
from empleados.utils.rol import Rol


class Menu:
    zoologico = Zoologico()

    def mostrar_menu(self):
        while True:
            print("\n---BIENVENIDO---\n")
            print("Selecciona una opcion\n")
            print("1. Registrar empleado")
            print("2. Registrat visitante")
            print("4. Registrar visita")
            print("5. Salir")

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
                
            elif opcion == "4":
                print("\n Selecionaste la opción de registrar visita\n")
                print("\nBoleto adulto: $100.00")
                print("\nBoleto niño: $50.00")

                #numero_visitas = 0
                #numero_visitas =+1
                #precio1 = 100 * adultos
                #precio2 = 50 * niños
                #precio_total = precio1 + precio2
                #descuento = precio_total * 0.20
                #precio_final = precio_total - descuento


                

            elif opcion == "5":
                print("\nAdios!!!\n")
                break
            else:
                print("\nOpcion no valida, intente de nuevo\n")