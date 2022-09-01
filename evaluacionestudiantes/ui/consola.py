import sys

from evaluacionestudiantes.modelo.evaluacion import Curso


class UiConsola:
    """
    Muestra un menú en pantalla y responde a las opciones que seleccione el usuario
    """

    def __init__(self) -> None:
        self.curso = Curso("Algoritmos y Programación Orientada a Objetos")
        self.opciones = {
            "1": self.agregar_evento_evaluativo,
            "2": self.registrar_estudiante,
            "3": self.agregar_calificacion_a_estudiante,
            "4": self.estudiante_con_mejor_promedio,
            "5": self.evaluaciones_faltantes_de_estudiante,
            "0": self.salir
        }

    def mostrar_menu(self):
        print("""
        \n
        ====================================
        Menú de la aplicación para el manejo de evaluaciones del curso\n
        1. Agregar evento evaluativo
        2. Registrar estudiante
        3. Agregar calificación a estudiante
        4. Ver estudiante con mejor promedio
        5. Ver evaluaciones faltantes de estudiante
        0. Salir
        ====================================
        """)

    def ejecutar(self):
        """
        Muestra el menú y responde a la selección del usuario
        """
        while True:
            self.mostrar_menu()
            opcion = input("Seleccion una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida.")

    def agregar_evento_evaluativo(self):
        print(">>> AGREGAR EVENTO EVALUATIVO")
        print("Ingrese la información del evento\n")
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        porcentaje = float(input("Porcentaje: "))
        if self.curso.se_puede_agregar_evento_con_porcentaje(porcentaje):
            if self.curso.agregar_evento_evaluativo(codigo, nombre, descripcion, porcentaje):
                print(f"INFO: Se agregó el evento evaluativo con código {codigo}")
            else:
                print(f"ERROR: No se pudo agregar el evento porque ya existe uno con el mismo código.")
        else:
            print("ERROR: No se puede agregar el evento porque se sobrepasa el porcentaje de 100%")

    def registrar_estudiante(self):
        print(">>> REGISTRAR ESTUDIANTE")
        print("Ingrese la información del estudiante\n")
        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")

        if self.curso.registrar_estudiante(identificacion, nombre):
            print(f"INFO: Se registró el estudiante con éxito")
        else:
            print(f"ERROR: No se pudo registrar el estudiante porque ya existe uno con la misma identificación.")

    def agregar_calificacion_a_estudiante(self):
        print(">>> AGREGAR CALIFICACIÓN A ESTUDIANTE")

        identificacion = input("Identificación del estudiante: ")

        print("\nEventos evaluativos")
        for evento in self.curso.eventos_evaluativos:
            print(f"- {str(evento)}")

        codigo_evento = input("Código del evento: ")

        calificacion = float(input("Calificación: "))

        self.curso.agregar_calificacion_a_estudiante(identificacion, codigo_evento, calificacion)

    def estudiante_con_mejor_promedio(self):
        print(">>> ESTUDIANTE CON MEJOR PROMEDIO")
        estudiante = self.curso.estudiante_con_mejor_promedio()
        print(estudiante)

    def evaluaciones_faltantes_de_estudiante(self):
        print(">>> EVALUACIONES FALTANTES DE ESTUDIANTE")
        identificacion = input("Identificación del estudiante: ")
        eventos = self.curso.evaluaciones_faltantes_de_estudiante(identificacion)
        for evento in eventos:
            print(f"- {str(evento)}")

    def salir(self):
        print("\nGRACIAS POR USAR LA APLICACIÓN")
        sys.exit(0)
