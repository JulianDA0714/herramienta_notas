estudiantes = []

def agregar_estudiante(nombre, nota):
    estudiantes.append({"nombre": nombre, "nota": nota})

def listar_estudiantes():
    for e in estudiantes:
        print(f"  {e['nombre']}: {e['nota']}")
