"""Excepciones personalizadas para el sistema Software FJ."""

class ErrorSistema(Exception):
    """Excepción base para los errores controlados de la aplicación."""

class ErrorValidacion(ErrorSistema):
    """Se genera cuando un dato no cumple las reglas del sistema."""

class ClienteNoEncontrado(ErrorSistema):
    """Se genera cuando no existe el cliente solicitado."""

class ServicioNoDisponible(ErrorSistema):
    """Se genera cuando el servicio no está disponible."""

class ReservaInvalida(ErrorSistema):
    """Se genera cuando una reserva no puede crearse o procesarse."""

class OperacionNoPermitida(ErrorSistema):
    """Se genera cuando se intenta realizar una operación no permitida."""
