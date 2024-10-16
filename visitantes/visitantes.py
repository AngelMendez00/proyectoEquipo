from datetime import date
from empleados.empleado import Empleado
from random import randint



class Visitante:
    id: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date
    curp: str
    numero_visitas: int
    fecha_registro: date

    def __init__(self, id:str,
                 nombre: str, 
                 apellidos: str, 
                 fecha_nacimiento: date, 
                 curp: str, 
                 numero_visitas: int, 
                 fecha_registro: date):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.curp = curp
        self.numero_visitas = numero_visitas
        self.fecha_registro = fecha_registro
        self.id = id

    def mostrar_info_visitante(self):
        nombre_completo = f"{self.nombre} {self.apellidos}"
        info = f"\n-ID: {self.id}\n-Nombre completo: {nombre_completo}\n-Fecha de nacimiento: {self.fecha_nacimiento}\n-Curp: {self.curp}\n-Número de visitas: {self.numero_visitas}\n-Fecha de registro: {self.fecha_registro}"
        return info