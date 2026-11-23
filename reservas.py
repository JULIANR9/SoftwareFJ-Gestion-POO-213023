"""Clase Reserva y operaciones sobre su estado."""
from datetime import datetime
from entidades import Entidad
from excepciones import ReservaInvalida, OperacionNoPermitida

class Reserva(Entidad):
    ESTADOS = {"CREADA", "CONFIRMADA", "CANCELADA", "PROCESADA"}

    def __init__(self, identificador, cliente, servicio, cantidad):
        super().__init__(identificador)
        if cliente is None or servicio is None:
            raise ReservaInvalida("La reserva requiere un cliente y un servicio.")
        servicio.validar_parametros(cantidad)
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.estado = "CREADA"
        self.fecha_creacion = datetime.now().isoformat(timespec="seconds")
        self.total = None

    def confirmar(self):
        if self.estado != "CREADA":
            raise OperacionNoPermitida("Solo se pueden confirmar reservas recién creadas.")
        self.estado = "CONFIRMADA"

    def cancelar(self):
        if self.estado == "PROCESADA":
            raise OperacionNoPermitida("No se puede cancelar una reserva procesada.")
        if self.estado == "CANCELADA":
            raise OperacionNoPermitida("La reserva ya está cancelada.")
        self.estado = "CANCELADA"

    def procesar(self, impuesto=0.19, descuento=0.0):
        if self.estado != "CONFIRMADA":
            raise OperacionNoPermitida("La reserva debe estar confirmada antes de procesarse.")
        self.total = self.servicio.calcular_costo(self.cantidad, impuesto, descuento)
        self.estado = "PROCESADA"
        return self.total

    def describir(self):
        return (f"Reserva {self.identificador} | {self.cliente.nombre} | "
                f"{self.servicio.nombre} | Estado: {self.estado} | Total: {self.total}")
