from datetime import datetime

class Comida:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes  # Lista de strings
        self.creada = datetime.now().isoformat()

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "ingredientes": self.ingredientes,
            "creada": self.creada
        }

    @staticmethod
    def from_dict(data):
        comida = Comida(data["nombre"], data["ingredientes"])
        comida.creada = data.get("creada", datetime.now().isoformat())
        return comida

    def __str__(self):
        return f"{self.nombre} ({', '.join(self.ingredientes)})"


class DiaSemana:
    def __init__(self, dia):
        self.dia = dia  # 'Lunes', 'Martes', etc.
        self.comidas = []  # Lista de objetos Comida

    def agregar_comida(self, comida):
        self.comidas.append(comida)

    def to_dict(self):
        return {
            "dia": self.dia,
            "comidas": [c.to_dict() for c in self.comidas]
        }

    @staticmethod
    def from_dict(data):
        dia = DiaSemana(data["dia"])
        dia.comidas = [Comida.from_dict(c) for c in data["comidas"]]
        return dia

    def __str__(self):
        return f"{self.dia}: " + "; ".join(str(c) for c in self.comidas)


class PlanSemanal:
    def __init__(self):
        self.dias = {dia: DiaSemana(dia) for dia in [
            "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"
        ]}

    def agregar_comida_a_dia(self, dia, comida):
        if dia in self.dias:
            self.dias[dia].agregar_comida(comida)
        else:
            raise ValueError(f"Día inválido: {dia}")

    def to_dict(self):
        return {dia: self.dias[dia].to_dict() for dia in self.dias}

    @staticmethod
    def from_dict(data):
        plan = PlanSemanal()
        for dia in data:
            plan.dias[dia] = DiaSemana.from_dict(data[dia])
        return plan

    def __str__(self):
        return "\n".join(str(self.dias[d]) for d in self.dias)
