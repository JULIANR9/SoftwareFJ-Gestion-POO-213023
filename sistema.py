"""Gestor principal, listas internas y registro de eventos."""
import logging
from logging.handlers import RotatingFileHandler
from excepciones import (ErrorSistema, ErrorValidacion, ClienteNoEncontrado,
                         ServicioNoDisponible, ReservaInvalida)
from entidades import Cliente
from servicios import Servicio
from reservas import Reserva

logger = logging.getLogger("SoftwareFJ")
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler("software_fj.log", maxBytes=100_000, backupCount=2, encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
    logger.addHandler(handler)

class SistemaFJ:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        try:
            if not isinstance(cliente, Cliente):
                raise ErrorValidacion("El objeto recibido no es un cliente válido.")
            if any(c.identificador == cliente.identificador for c in self.clientes):
                raise ErrorValidacion("Ya existe un cliente con ese identificador.")
            self.clientes.append(cliente)
            logger.info("Cliente registrado: %s", cliente.identificador)
        except ErrorSistema as error:
            logger.exception("No se pudo registrar el cliente")
            raise
        else:  # Se ejecuta únicamente cuando no ocurre una excepción.
            logger.info("Registro de cliente finalizado correctamente")
            return cliente

    def buscar_cliente(self, identificador):
        for cliente in self.clientes:
            if cliente.identificador == str(identificador):
                return cliente
        raise ClienteNoEncontrado(f"No existe el cliente {identificador}.")

    def registrar_servicio(self, servicio):
        try:
            if not isinstance(servicio, Servicio):
                raise ErrorValidacion("El objeto recibido no es un servicio válido.")
            if any(s.identificador == servicio.identificador for s in self.servicios):
                raise ErrorValidacion("Ya existe un servicio con ese identificador.")
            self.servicios.append(servicio)
            logger.info("Servicio registrado: %s", servicio.identificador)
            return servicio
        except ErrorSistema:
            logger.exception("No se pudo registrar el servicio")
            raise

    def buscar_servicio(self, identificador):
        for servicio in self.servicios:
            if servicio.identificador == str(identificador):
                return servicio
        raise ServicioNoDisponible(f"No existe el servicio {identificador}.")

    def crear_reserva(self, identificador, id_cliente, id_servicio, cantidad):
        try:
            cliente = self.buscar_cliente(id_cliente)
            servicio = self.buscar_servicio(id_servicio)
            reserva = Reserva(identificador, cliente, servicio, cantidad)
            if any(r.identificador == reserva.identificador for r in self.reservas):
                raise ReservaInvalida("Ya existe una reserva con ese identificador.")
            self.reservas.append(reserva)
            logger.info("Reserva creada: %s", identificador)
            return reserva
        except (ErrorSistema, TypeError, ValueError) as error:
            logger.exception("Error al crear reserva %s", identificador)
            # Encadenamiento: conserva la causa original y añade contexto.
            raise ReservaInvalida(f"No fue posible crear la reserva {identificador}.") from error

    def confirmar_reserva(self, identificador):
        reserva = self.buscar_reserva(identificador)
        try:
            reserva.confirmar()
            logger.info("Reserva confirmada: %s", identificador)
        except ErrorSistema:
            logger.exception("Error al confirmar reserva %s", identificador)
            raise

    def procesar_reserva(self, identificador, impuesto=0.19, descuento=0.0):
        reserva = self.buscar_reserva(identificador)
        try:
            total = reserva.procesar(impuesto, descuento)
            logger.info("Reserva procesada: %s. Total: %.2f", identificador, total)
            return total
        except ErrorSistema:
            logger.exception("Error al procesar reserva %s", identificador)
            raise
        finally:
            # Se ejecuta tanto si el procesamiento funciona como si falla.
            logger.info("Finalizó intento de procesamiento de reserva %s", identificador)

    def cancelar_reserva(self, identificador):
        reserva = self.buscar_reserva(identificador)
        try:
            reserva.cancelar()
            logger.warning("Reserva cancelada: %s", identificador)
        except ErrorSistema:
            logger.exception("Error al cancelar reserva %s", identificador)
            raise

    def buscar_reserva(self, identificador):
        for reserva in self.reservas:
            if reserva.identificador == str(identificador):
                return reserva
        raise ReservaInvalida(f"No existe la reserva {identificador}.")

    def resumen(self):
        return {"clientes": len(self.clientes), "servicios": len(self.servicios),
                "reservas": len(self.reservas)}
