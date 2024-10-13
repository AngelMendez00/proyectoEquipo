from datetime import time
from datetime import date
from empleados.utils.rol import Rol
from usuarios.usuario import Usuario
from random import randint

class Empleado(Usuario):
 
    fecha_inicio: date
    rfc: str
    salario: float
    horario: time
    rol: Rol

    def __init__(self, nombre: str, apellidos: str, fecha_nacimiento: date, fecha_inicio: date, rfc: str, curp: str, salario: float, horario: time, rol: Rol):
        super().__init__(id=self.generar_id(nombre=nombre,rol=rol), nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento, curp=curp)
        self.fecha_inicio = fecha_inicio
        self.rfc = rfc
        self.salario = salario
        self.horario = horario
        self.rol = rol

    def generar_id(self, nombre: str, rol: Rol):
        iniciales_nombre=nombre[0:3].upper()
        id=f"{iniciales_nombre}{rol.value}{randint(0,5000)}"
        return id
    
    def mostrar_info(self):
        nombre_completo= f"{self.nombre} {self.apellidos}"
        info=f"\n-ID: {self.id}\n-Nombre completo: {nombre_completo}\n-Fecha de nacimiento: {self.fecha_nacimiento}\n-Fecha de inicio: {self.fecha_inicio}\n-RFC: {self.rfc}\n-CURP: {self.curp}\n-Salario: {self.salario}"
        return info