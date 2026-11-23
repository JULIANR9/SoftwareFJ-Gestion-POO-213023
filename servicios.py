"""Servicios especializados ofrecidos por Software FJ."""
from abc import ABC, abstractmethod
from entidades import Entidad
from excepciones import ErrorValidacion

class Servicio(Entidad, ABC):
    def __init__(self, identificador, nombre, tarifa_base):
        super().__init__(identificador)
        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorValidacion("El nombre del servicio es obligatorio.")
        if not isinstance(tarifa_base, (int, float)) or tarifa_base <= 0:
            raise ErrorValidacion("La tarifa base debe ser un número positivo.")
        self.nombre = nombre.strip()
        self.tarifa_base = float(tarifa_base)

    @abstractmethod
    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0):
        """Calcula el costo según las características del servicio."""
        raise NotImplementedError

    @abstractmethod
    def validar_parametros(self, cantidad):
        raise NotImplementedError

    def describir(self):
        return f"{self.nombre} (código {self.identificador})"

class ReservaSala(Servicio):
    def validar_parametros(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad <= 0 or cantidad > 12:
            raise ErrorValidacion("La duración de la sala debe ser de 1 a 12 horas.")

    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0):
        self.validar_parametros(cantidad)
        return _calcular(self.tarifa_base * cantidad, impuesto, descuento)

class AlquilerEquipo(Servicio):
    def validar_parametros(self, cantidad):
        if not isinstance(cantidad, int) or cantidad < 1 or cantidad > 20:
            raise ErrorValidacion("La cantidad de equipos debe ser un entero entre 1 y 20.")

    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0):
        self.validar_parametros(cantidad)
        return _calcular(self.tarifa_base * cantidad, impuesto, descuento)

class AsesoriaEspecializada(Servicio):
    def validar_parametros(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad <= 0 or cantidad > 40:
            raise ErrorValidacion("La asesoría debe tener entre 1 y 40 horas.")

    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0):
        self.validar_parametros(cantidad)
        return _calcular(self.tarifa_base * cantidad, impuesto, descuento)

def _calcular(subtotal, impuesto, descuento):
    """Aplica porcentajes y valida que el cálculo sea consistente."""
    if not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 1:
        raise ErrorValidacion("El impuesto debe expresarse entre 0 y 1.")
    if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 1:
        raise ErrorValidacion("El descuento debe expresarse entre 0 y 1.")
    total = subtotal * (1 - descuento) * (1 + impuesto)
    if total < 0:
        raise ErrorValidacion("El cálculo produjo un valor inconsistente.")
    return round(total, 2)
