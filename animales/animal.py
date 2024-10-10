from datetime import datetime
from alimentacion import Alimentacion
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

    def __init__(self, id: str, tipo:str, fecha_llegada: str, enfermedades: List[str], tipo_alimentacion: Alimentacion, fecha_nacimiento: datetime, peso:float, frecuencia_alimentacion: int, vacunas: bool ):
        self.id = id
        self.tipo = tipo
        self.fecha_llegada = fecha_llegada
        self.enfermedades = enfermedades
        self.tipo_alimentacio = tipo_alimentacion
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self.vacunas = vacunas


    def generar_id_animal(self, tipo, fecha_llegada):
        id = f"AN{tipo[:2].upper()}{str(fecha_llegada[-2:])}{randint(1,10000)}{datetime.now().day}"
        return id