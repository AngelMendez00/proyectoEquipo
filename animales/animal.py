from datetime import datetime
from utils.alimentacion import Alimentacion
from typing import List
from random import randint

class Animal:

    id: str
    tipo: str
    fecha_llegada: datetime
    enfermedades: List[str] = []
    tipo_alimentacion: Alimentacion
    fecha_nacimiento: datetime
    peso: float
    frecuencia_alimentacion: int
    vacunas: bool

    def __init__(self, tipo:str, fecha_llegada: str, enfermedades: List[str], tipo_alimentacion: Alimentacion, fecha_nacimiento: datetime, peso:float, frecuencia_alimentacion: int, vacunas: bool ):
        self.id = self.generar_id_animal(tipo=tipo, fecha_llegada=fecha_llegada, fecha_nacimiento=fecha_nacimiento)
        self.tipo = tipo
        self.fecha_llegada = fecha_llegada
        self.enfermedades = enfermedades
        self.tipo_alimentacion = tipo_alimentacion
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self.vacunas = vacunas


    def generar_id_animal(self, tipo, fecha_llegada, fecha_nacimiento):
        id = f"AN{tipo[:2].upper()}{str(fecha_llegada[-2:])}{str(fecha_nacimiento[:2])}{randint(1,10000)}{datetime.now().day}"
        return id
    
    def mostrar_info_animal(self):
        info = f"""Animal: {self.tipo} ID: {self.id} 
                   Fecha de llegada: {self.fecha_llegada}
                   Enfermedades: {self.enfermedades}
                   Tipo de alimentacion: {self.tipo_alimentacion}
                   Fecha de nacimiento: {self.fecha_nacimiento}
                   Peso: {self.peso}
                   Vacunado: {self.vacunas}"""
        return info
        
