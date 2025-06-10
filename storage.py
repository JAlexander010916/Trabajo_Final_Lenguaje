import aiofiles
import json
import os
from models import Comida, PlanSemanal

COMIDAS_PATH = "data/comidas.json"
PLAN_PATH = "data/plan.json"

async def guardar_comidas(comidas):
    os.makedirs("data", exist_ok=True)
    async with aiofiles.open(COMIDAS_PATH, mode="w") as f:
        data = [c.to_dict() for c in comidas]
        await f.write(json.dumps(data, indent=4))

async def cargar_comidas():
    if not os.path.exists(COMIDAS_PATH):
        return []
    async with aiofiles.open(COMIDAS_PATH, mode="r") as f:
        contenido = await f.read()
        try:
            data = json.loads(contenido)
            return [Comida.from_dict(c) for c in data]
        except json.JSONDecodeError:
            return []

async def guardar_plan(plan):
    os.makedirs("data", exist_ok=True)
    async with aiofiles.open(PLAN_PATH, mode="w") as f:
        await f.write(json.dumps(plan.to_dict(), indent=4))

async def cargar_plan():
    if not os.path.exists(PLAN_PATH):
        return PlanSemanal()
    async with aiofiles.open(PLAN_PATH, mode="r") as f:
        contenido = await f.read()
        try:
            data = json.loads(contenido)
            return PlanSemanal.from_dict(data)
        except json.JSONDecodeError:
            return PlanSemanal()
