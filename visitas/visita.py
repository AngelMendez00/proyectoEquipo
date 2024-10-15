from empleados.empleado import Empleado
from visitantes.visitantes import Visitante
from random import randint
from typing import List
from datetime import date

class Visita: 
    id: str
    guia_a_cargo: Empleado
    costo_total: float
    visitantes: List[Visitante]=[]
    fecha_visita: date
    cantidad_adultos: int
    cantidad_niños: int

    def __init__(self, 
                 guia_a_cargo: Empleado, 
                 costo_total: float,
                 visitantes: List[Visitante],
                 fecha_visita: date,
                 cantidad_adultos: int,
                 cantidad_niños: int):
        self.id = self.generar_id_visita(guia_a_cargo=guia_a_cargo)
        self.guia_a_cargo = guia_a_cargo
        self.costo_total = costo_total
        self.visitantes = visitantes
        self.fecha_visita = fecha_visita
        self.cantidad_adultos = cantidad_adultos
        self.cantidad_niños = cantidad_niños

    def generar_id_visita (self, guia_a_cargo: Empleado):
        nombre = guia_a_cargo.nombre
        id = f"{nombre[:2].upper()}{randint(0,10000)}"
        return id

    def mostrar_info_visita(self):
        info = f"""
                ID de visita: {self.id}
                ID del guia a cargo: {self.guia_a_cargo.id} 
                Nombre de guia a cargo: {self.guia_a_cargo.nombre}
                Fecha de realizacion de la visita: {self.fecha_visita}
                Costo total de visita: {self.costo_total}
                Cantidad de adultos: {self.cantidad_adultos}
                Cantidad de niños: {self.cantidad_niños}
                """
        return info
