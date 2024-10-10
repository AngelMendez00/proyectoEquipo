from empleados.empleado import Empleado
from veterinario.veterinario import Veterinario
from mantenimiento.mantenimiento import Mantenimiento
from administracion.administracion import Administracion
from guia.guia import Guia
from typing import List


class Zoologico:
    lista_empleados:List[Empleado]=[]
    lista_veterinario:List[Veterinario]=[]
    lista_guia:List[Guia]=[]
    lista_mantenimiento:List[Mantenimiento]=[]
    lista_administracion:List[Administracion]=[]

    def __init__(self):
        pass

            