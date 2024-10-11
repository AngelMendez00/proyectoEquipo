from empleados.empleado import Empleado
from datetime import datetime
from empleados.utils.rol import Rol

class Mantenimiento(Empleado):
    

    def __init__(self, nombre: str, 
                apellidos: str, 
                fecha_nacimiento: datetime, 
                fecha_inicio: datetime, 
                rfc: str, 
                curp: str, 
                salario: float, 
                horario: datetime):
        super().__init__(nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento, fecha_inicio=fecha_inicio, rfc=rfc, curp=curp, salario=salario, horario=horario, rol=Rol.MANTENIMIENTO)