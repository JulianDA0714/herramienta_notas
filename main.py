from estudiantes import estudiantes, agregar_estudiante, listar_estudiantes
from exportar import exportar_pdf

# Agregar estudiantes de prueba
nombres = [
    "Ana García", "Luis Martínez", "María López", "Carlos Pérez",
    "Sofía Rodríguez", "Andrés Torres", "Valentina Gómez", "Diego Hernández",
    "Isabella Díaz", "Santiago Vargas", "Camila Jiménez", "Sebastián Castro",
    "Lucía Moreno", "Mateo Romero", "Paula Gutiérrez", "Nicolás Sánchez",
    "Daniela Ramírez", "Felipe Ortiz", "Laura Flores", "Juan Mendoza",
    "Alejandra Reyes", "Esteban Cruz", "Natalia Vega", "Tomás Aguilar",
    "Gabriela Silva", "Ricardo Molina", "Mariana Rojas", "Javier Núñez",
    "Catalina Herrera", "Andrés Medina", "Paola Suárez", "Oscar Guerrero",
]

for i, nombre in enumerate(nombres):
    agregar_estudiante(nombre, round(3.0 + (i % 20) * 0.1, 1))

print(f"Total de estudiantes: {len(estudiantes)}")
print("Lista de estudiantes:")
listar_estudiantes()

print()
print("Intentando exportar PDF...")
exportar_pdf(estudiantes)
