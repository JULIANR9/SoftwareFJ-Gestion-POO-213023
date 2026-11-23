# Software FJ - Sistema Integral de Gestión de Clientes, Servicios y Reservas

Proyecto académico de Programación (UNAD, código 213023), Fase 4.

## Requisitos
- Python 3.10 o superior.
- No requiere instalar librerías externas.

## Ejecución
Desde esta carpeta, ejecute:

```bash
python main.py
```

El programa crea automáticamente `software_fj.log` para registrar eventos y errores.

## Archivos
- `excepciones.py`: excepciones personalizadas.
- `entidades.py`: clase abstracta Entidad y clase Cliente.
- `servicios.py`: clase abstracta Servicio y tres servicios especializados.
- `reservas.py`: gestión del ciclo de vida de las reservas.
- `sistema.py`: listas internas, operaciones y logging.
- `main.py`: demostración de operaciones válidas e inválidas.
- `SoftwareFJ_Fase4.ipynb`: notebook con explicación y ejecución del proyecto.

## Características implementadas
- Abstracción, herencia, encapsulación y polimorfismo.
- Validaciones y excepciones personalizadas.
- Bloques `try/except`, `try/except/else`, `try/except/finally`.
- Encadenamiento de excepciones mediante `raise ... from error`.
- Registro de eventos y errores con `logging` y rotación de archivos.
- Más de diez simulaciones de operaciones válidas e inválidas.
- Sin base de datos: utiliza objetos y listas en memoria.

## Nota sobre sobrecarga
Python no implementa sobrecarga tradicional por firma como otros lenguajes. En este proyecto, `calcular_costo` admite parámetros opcionales para calcular el costo base, aplicar impuestos y aplicar descuentos en diferentes combinaciones.
