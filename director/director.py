from usuarios.usuario import Usuario
from datetime import datetime

class Director(Usuario):
    contraseña: str

    def __init__(self, id:str, nombre: str, apellidos: str, fecha_nacimiento: datetime, curp: str, contraseña: str):
          super().__init__(id=id,
               nombre=nombre,
               apellidos=apellidos,
               fecha_nacimiento=fecha_nacimiento,
               curp=curp
          )
          self.contraseña=contraseña
    def mostrar_info_director(self):
        nombre_completo = f"{self.nombre} {self.apellidos}"
        info = f"\n - Nombre completo: {nombre_completo}, CURP: {self.curp}, Fecha de nacimiento: {self.fecha_nacimiento}, Contraseña: {self.contraseña}"
        return info