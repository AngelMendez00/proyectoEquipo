from datetime import datetime


class Usuario:
    id: str
    nombre: str
    apellidos: str
    curp: str
    fecha_nacimiento: datetime
    
    
    def __init__(self, id:str, nombre: str, apellidos: str, fecha_nacimiento: datetime, curp: str):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.curp = curp
       
        