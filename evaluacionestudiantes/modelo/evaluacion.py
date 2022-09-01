class EventoEvaluativo:

    def __init__(self, codigo: str, nombre: str, descripcion: str, porcentaje: float):
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.porcentaje: float = porcentaje

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} ({self.porcentaje: .1f}%"


class Evaluacion:

    def __init__(self, evento: EventoEvaluativo, calificacion: float):
        self.evento: EventoEvaluativo = evento
        self.calificacion: float = calificacion

    def __str__(self) -> str:
        return f"{str(self.evento)}: {self.calificacion: .1f}"


class Estudiante:

    def __init__(self, identificacion: str, nombre: str):
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.evaluaciones: list[Evaluacion] = []

    def calcular_promedio(self) -> float:
        calificaciones = [(e.calificacion, e.evento.porcentaje) for e in self.evaluaciones]
        promedio: float = 0
        for c in calificaciones:
            promedio += c[0] * (c[1] / 100)
        return promedio

    def agregar_evaluacion(self, evento: EventoEvaluativo, calificacion: float):
        evaluacion = Evaluacion(evento, calificacion)
        self.evaluaciones.append(evaluacion)

    def __str__(self) -> str:
        return f"{self.identificacion} - {self.nombre}"


class Curso:

    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.eventos_evaluativos: dict[str, EventoEvaluativo] = {}
        self.estudiantes: dict[str, Estudiante] = {}

    def se_puede_agregar_evento_con_porcentaje(self, porcentaje: float):
        suma_porcentaje = sum([p.porcentaje for p in self.eventos_evaluativos.values()])
        return (suma_porcentaje + porcentaje) <= 100

    def agregar_evento_evaluativo(self, codigo: str, nombre: str, descripcion: str, porcentaje: float):
        if codigo not in self.eventos_evaluativos.keys():
            evento: EventoEvaluativo = EventoEvaluativo(codigo, nombre, descripcion, porcentaje)
            self.eventos_evaluativos[codigo] = evento
            return True
        else:
            return False

    def registrar_estudiante(self, identificacion: str, nombre: str):
        if identificacion not in self.estudiantes.keys():
            estudiante: Estudiante = Estudiante(identificacion, nombre)
            self.estudiantes[identificacion] = estudiante
            return True
        else:
            return False

    def agregar_calificacion_a_estudiante(self, identificacion: str, codigo_evento: str, calificacion: float):
        if identificacion in self.estudiantes.keys():
            estudiante = self.estudiantes[identificacion]
            evento = self.eventos_evaluativos[codigo_evento]
            estudiante.agregar_evaluacion(evento, calificacion)

    def estudiante_con_mejor_promedio(self) -> Estudiante:
        promedio_mayor = 0
        mejor_estudiante = None
        for estudiante in self.estudiantes.values():
            promedio = estudiante.calcular_promedio()
            if promedio > promedio_mayor:
                promedio_mayor = promedio
                mejor_estudiante = estudiante
        return mejor_estudiante

    def evaluaciones_faltantes_de_estudiante(self, identificacion: str) -> list[EventoEvaluativo]:
        evaluaciones_faltantes: list[EventoEvaluativo] = []
        if identificacion in self.estudiantes.keys():
            estudiante = self.estudiantes[identificacion]
            eventos_evaluados: list[EventoEvaluativo] = [e.evento for e in estudiante.evaluaciones]
            for evento in self.eventos_evaluativos:
                if evento not in eventos_evaluados:
                    evaluaciones_faltantes.append(evento)
            return evaluaciones_faltantes
        else:
            return None



