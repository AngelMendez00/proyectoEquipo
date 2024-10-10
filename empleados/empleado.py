from datetime import datetime
from empleados.utils.rol import Rol

class Empleado:
    nombre: str
    apellidos: str
    fecha_nacimiento: datetime
    fecha_inicio: datetime
    rfc: str
    curp: str
    salario: float
    horario: datetime
    rol: Rol

    def __init__(self, nombre: str, apellidos: str, fecha_nacimiento: datetime, fecha_inicio: datetime, rfc: str, curp: str, salario: float, horario: datetime, rol: Rol):
        self.nombre=nombre
        self.apellidos=apellidos
        self.fecha_nacimiento=fecha_nacimiento
        self.fecha_inicio=fecha_inicio
        self.rfc=rfc
        self.curp=curp
        self.salario=salario
        self.horario=horario
        self.rol=rol