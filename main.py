import asyncio
from models import Comida
from logic import generar_plan_aleatorio, buscar_comidas_por_ingrediente, filtrar_comidas_por_nombre
from storage import (
    cargar_comidas,
    guardar_comidas,
    cargar_plan,
    guardar_plan
)

comidas = []
plan = None

async def inicializar():
    global comidas, plan
    comidas = await cargar_comidas()
    plan = await cargar_plan()
    print("Datos cargados exitosamente.\n")


def mostrar_menu():
    print("Planificador de Comidas Semanal")
    print("1. Agregar nueva comida")
    print("2. Ver todas las comidas")
    print("3. Buscar comidas por ingrediente")
    print("4. Generar plan semanal aleatorio")
    print("5. Ver plan semanal actual")
    print("6. Eliminar una comida")
    print("7. Guardar y salir")


def agregar_comida():
    nombre = input("Nombre de la comida: ")
    ingredientes = input("Lista de ingredientes (separados por coma): ").split(",")
    ingredientes = [i.strip() for i in ingredientes if i.strip()]
    comida = Comida(nombre, ingredientes)
    comidas.append(comida)
    print("✅ Comida agregada.")


def ver_comidas():
    if not comidas:
        print("No hay comidas registradas.")
    else:
        for i, comida in enumerate(comidas, 1):
            print(f"{i}. {comida}")


def eliminar_comida():
    ver_comidas()
    if not comidas:
        return

    print("Escribe el número de la comida que deseas eliminar.")
    print("Escribe 'A' para volver al menú principal.")

    entrada = input("Tu opción: ").strip()

    if entrada.lower() == "a":
        print("↩️ Regresando al menú principal.")
        return

    try:
        idx = int(entrada)
        if 1 <= idx <= len(comidas):
            eliminada = comidas.pop(idx - 1)
            print(f"✅ Comida eliminada: {eliminada.nombre}")
        else:
            print("⚠️ Índice fuera de rango.")
    except ValueError:
        print("⚠️ Entrada no válida.")


def buscar_por_ingrediente():
    ing = input("Ingrediente a buscar: ")
    resultados = buscar_comidas_por_ingrediente(comidas, ing)
    if resultados:
        for c in resultados:
            print(f"- {c}")
    else:
        print("No se encontraron comidas con ese ingrediente.")


def generar_plan():
    try:
        nuevo_plan = generar_plan_aleatorio(comidas)
        global plan
        plan = nuevo_plan
        print("✅ Plan generado exitosamente.")
    except ValueError as e:
        print(f"⚠️ {e}")


def ver_plan():
    if plan:
        print("\n🍽️ Plan Semanal:\n")
        print(plan)
    else:
        print("No hay plan semanal generado.")


async def main():
    await inicializar()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_comida()
        elif opcion == "2":
            ver_comidas()
        elif opcion == "3":
            buscar_por_ingrediente()
        elif opcion == "4":
            generar_plan()
        elif opcion == "5":
            ver_plan()
        elif opcion == "6":
            eliminar_comida()
        elif opcion == "7":
            await guardar_comidas(comidas)
            await guardar_plan(plan)
            print("✅ Datos guardados. ¡Hasta luego!")
            break

    else:
            print("Opción inválida.")

if __name__ == "__main__":
    asyncio.run(main())
