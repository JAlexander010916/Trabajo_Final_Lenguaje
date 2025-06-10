from random import choice, sample
from models import Comida, PlanSemanal


def generar_plan_aleatorio(comidas_disponibles, comidas_por_dia=2):

    if len(comidas_disponibles) < comidas_por_dia * 7:
        raise ValueError("No hay suficientes comidas para generar un plan completo.")

    plan = PlanSemanal()
    comidas_seleccionadas = sample(comidas_disponibles, comidas_por_dia * 7)

    dias = list(plan.dias.keys())
    idx = 0
    for dia in dias:
        for _ in range(comidas_por_dia):
            plan.agregar_comida_a_dia(dia, comidas_seleccionadas[idx])
            idx += 1
    return plan


def buscar_comidas_por_ingrediente(comidas, ingrediente):

    return list(filter(lambda c: ingrediente.lower() in [i.lower() for i in c.ingredientes], comidas))


def filtrar_comidas_por_nombre(comidas, texto):

    return [c for c in comidas if texto.lower() in c.nombre.lower()]
