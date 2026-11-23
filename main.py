"""Punto de entrada: demostración con operaciones válidas e inválidas."""
from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from sistema import SistemaFJ
from excepciones import ErrorSistema


def ejecutar_pruebas():
    sistema = SistemaFJ()
    print("=== SISTEMA SOFTWARE FJ ===")

    # 1. Registro válido de cliente.
    try:
        sistema.registrar_cliente(Cliente("C001", "Laura Pérez", "laura@email.com", "3001234567"))
        print("1. Cliente C001 registrado.")
    except ErrorSistema as e:
        print("1. Error controlado:", e)

    # 2. Registro inválido de cliente: correo incorrecto.
    try:
        sistema.registrar_cliente(Cliente("C002", "Carlos Ruiz", "correo-invalido", "3111234567"))
    except ErrorSistema as e:
        print("2. Cliente inválido rechazado:", e)

    # 3. Registro válido de segundo cliente.
    try:
        sistema.registrar_cliente(Cliente("C003", "Andrés Gómez", "andres@email.com", "3207654321"))
        print("3. Cliente C003 registrado.")
    except ErrorSistema as e:
        print("3. Error controlado:", e)

    # 4. Registro válido de sala.
    try:
        sistema.registrar_servicio(ReservaSala("S001", "Sala de reuniones", 50000))
        print("4. Servicio de sala registrado.")
    except ErrorSistema as e:
        print("4. Error controlado:", e)

    # 5. Registro válido de alquiler de equipos.
    try:
        sistema.registrar_servicio(AlquilerEquipo("S002", "Alquiler de portátil", 30000))
        print("5. Servicio de equipos registrado.")
    except ErrorSistema as e:
        print("5. Error controlado:", e)

    # 6. Registro válido de asesoría.
    try:
        sistema.registrar_servicio(AsesoriaEspecializada("S003", "Asesoría de software", 80000))
        print("6. Servicio de asesoría registrado.")
    except ErrorSistema as e:
        print("6. Error controlado:", e)

    # 7. Intento de crear un servicio con tarifa inválida.
    try:
        servicio_invalido = ReservaSala("S004", "Sala inválida", -1000)
        sistema.registrar_servicio(servicio_invalido)
    except ErrorSistema as e:
        print("7. Servicio inválido rechazado:", e)

    # 8. Crear y confirmar reserva válida.
    try:
        sistema.crear_reserva("R001", "C001", "S001", 2)
        sistema.confirmar_reserva("R001")
        print("8. Reserva R001 creada y confirmada.")
    except ErrorSistema as e:
        print("8. Error controlado:", e)

    # 9. Procesar reserva y calcular impuesto y descuento.
    try:
        total = sistema.procesar_reserva("R001", impuesto=0.19, descuento=0.10)
        print(f"9. Reserva R001 procesada. Total: ${total:,.2f}")
    except ErrorSistema as e:
        print("9. Error controlado:", e)

    # 10. Intentar cancelar una reserva ya procesada.
    try:
        sistema.cancelar_reserva("R001")
    except ErrorSistema as e:
        print("10. Cancelación no permitida controlada:", e)

    # 11. Crear reserva con servicio inexistente: prueba encadenamiento.
    try:
        sistema.crear_reserva("R002", "C001", "S999", 1)
    except ErrorSistema as e:
        print("11. Reserva inválida controlada:", e)
        if e.__cause__:
            print("    Causa original:", e.__cause__)

    # 12. Intentar procesar una reserva que no existe.
    try:
        sistema.procesar_reserva("R999")
    except ErrorSistema as e:
        print("12. Reserva inexistente controlada:", e)

    # 13. Reserva cancelada correctamente.
    try:
        sistema.crear_reserva("R003", "C003", "S002", 2)
        sistema.cancelar_reserva("R003")
        print("13. Reserva R003 cancelada correctamente.")
    except ErrorSistema as e:
        print("13. Error controlado:", e)

    print("Resumen:", sistema.resumen())
    print("La aplicación terminó sin detenerse por los errores controlados.")
    print("Revise software_fj.log para consultar los eventos y errores.")


if __name__ == "__main__":
    ejecutar_pruebas()
