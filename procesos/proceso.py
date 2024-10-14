from empleados.empleado import Empleado
from procesos.utils.tipos_procesos import TiposProcesos
from datetime import date

class Proceso:
    empleado_encargado: Empleado
    tipo_proceso: TiposProcesos
    observaciones: str
    fecha_proceso: date
    id_animal: str
    
    def __init__(self, empleado_encargado: Empleado, tipo_proceso: TiposProcesos, observaciones: str, fecha_proceso: date, id_animal:str):
        self.empleado_encargado = empleado_encargado
        self.tipo_proceso = tipo_proceso
        observaciones = observaciones
        fecha_proceso = fecha_proceso
        id_animal = id_animal
        
    def mostrar_info_proceso(self):
        info = f"""
                Tipo de proceso: {self.tipo_proceso}
                ID del animal: {self.id_animal} 
                Empleado encargado: {self.empleado_encargado}
                Fecha de realizacion del proceso: {self.fecha_proceso}
                Observaciones: {self.observaciones}
                """
        return info