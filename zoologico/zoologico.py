from empleados.empleado import Empleado
from visitantes.visitantes import Visitante
from visitas.visita import Visita
from usuarios.usuario import Usuario
from typing import List
from datetime import time
from datetime import date
from datetime import datetime
from datetime import date
from empleados.utils.rol import Rol


class Zoologico:
    lista_empleados:List[Empleado]=[]
    lista_usuario: List[Usuario]=[]
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
                visitante.numero_visitas +1
                return visitante
            else: 
                print("ID no encontrada")

    def validar_id_guia(self, id_guia:str):
        for empleado in self.lista_empleados:
            if id_guia == empleado.id:
                if empleado.rol == Rol.GUIA:
                    return empleado
                else: 
                    print("El empleado no es guia")
         
        print("ID no encontrada")






            