"""Entidades principales del sistema."""
from abc import ABC, abstractmethod
from excepciones import ErrorValidacion

class Entidad(ABC):
    """Clase abstracta que representa una entidad identificable."""
    def __init__(self, identificador):
        if not identificador or not str(identificador).strip():
            raise ErrorValidacion("El identificador no puede estar vacío.")
        self._identificador = str(identificador).strip()

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def describir(self):
        """Devuelve una descripción de la entidad."""
        raise NotImplementedError

class Cliente(Entidad):
    """Cliente con datos encapsulados y validaciones básicas."""
    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise ErrorValidacion("El nombre debe tener al menos dos caracteres.")
        self._nombre = valor.strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or "@" not in valor or "." not in valor.split("@")[-1]:
            raise ErrorValidacion("El correo electrónico no tiene un formato válido.")
        self._correo = valor.strip().lower()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        limpio = str(valor).replace(" ", "").replace("-", "")
        if not limpio.isdigit() or len(limpio) < 7:
            raise ErrorValidacion("El teléfono debe contener mínimo 7 dígitos.")
        self._telefono = limpio

    def describir(self):
        return f"Cliente {self.identificador}: {self.nombre} ({self.correo})"
