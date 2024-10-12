from datetime import datetime
from empleados.utils.rol import Rol
from usuarios.usuario import Usuario

class Empleado(Usuario):
 
    fecha_inicio: datetime
    rfc: str
    salario: float
    horario: datetime
    rol: Rol

    def __init__(self, id:str, nombre: str, apellidos: str, fecha_nacimiento: datetime, fecha_inicio: datetime, rfc: str, curp: str, salario: float, horario: datetime, rol: Rol):
        super().__init__(id=id, nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento, curp=curp)
        self.fecha_inicio = fecha_inicio
        self.rfc = rfc
        self.salario = salario
        self.horario = horario
        self.rol = rol
