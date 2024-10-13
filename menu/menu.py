from zoologico.zoologico import Zoologico
from empleados.empleado import Empleado
from usuarios.usuario import Usuario
from datetime import date
from datetime import time
from datetime import datetime
from empleados.utils.rol import Rol
from visitantes.visitantes import Visitante


class Menu:
    zoologico = Zoologico()

    def mostrar_menu(self):
        while True:
            print("\n---BIENVENIDO---\n")
            print("Selecciona una opcion\n")
            print("1. Registrar empleado")
            print("2. Registrar visitante")
            print("3. Salir")

            opcion=input("Opcion: ")

            if opcion == "1":
                print("\nSeleccionaste registrar empleado\n")

                print("\nSelecciona el tipo de empleado a registrar\n")
                print("1. Administrador")
                print("2. Mantenimiento")
                print("3. Veterinario")
                print("4. Guia")
                
                registrar=5

                while registrar>=5:
                    registrar= int(input("Tipo de empleado a registrar: "))
                    if registrar >= 5 :
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

                if registrar ==1:
                    rol=Rol.ADMINISTRACION
                elif registrar == 2:
                    rol=Rol.MANTENIMIENTO
                elif registrar == 3:
                    rol=Rol.VETERINARO
                elif registrar == 4:
                    rol=Rol.GUIA

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
                print("\nAdios!!!\n")
                break
            else:
                print("\nOpcion no valida, intente de nuevo\n")