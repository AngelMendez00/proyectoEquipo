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

    def __init__(self, 
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
        self.id = self.generar_id(nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento, fecha_registro=fecha_registro)

    def generar_id(self, nombre: str, apellidos: str, fecha_nacimiento:date, fecha_registro:date):
        iniciales_nombre=nombre[:2].upper()
        iniciales_apellidos=apellidos[:2].upper()
        id=f"{iniciales_nombre}{iniciales_apellidos}{randint(0, 10000)}{str(fecha_nacimiento.year)[-2:]}{str(fecha_registro.year)[-2:]}"
        return id

    def mostrar_info_visitante(self):
        nombre_completo = f"{self.nombre} {self.apellidos}"
        info = f"\n-ID: {self.id}\n-Nombre completo: {nombre_completo}\n-Fecha de nacimiento: {self.fecha_nacimiento}\n-Curp: {self.curp}\n-Número de visitas: {self.numero_visitas}\n-Fecha de registro: {self.fecha_registro}"
        return info