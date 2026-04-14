import time

def exportar_pdf(estudiantes):
    """
    Exporta la lista de estudiantes a un archivo PDF.
    """
    print("Generando PDF...")

    # Tiempo límite para generar el PDF
    tiempo_limite = 0.2  # segundos

    # Tiempo que tarda según la cantidad de estudiantes
    tiempo_generacion = len(estudiantes) * 0.01

    if tiempo_generacion > tiempo_limite:
        print("PDF generado: reporte_notas.pdf")
        print("(archivo vacío)")
        return False
    else:
        print("PDF generado correctamente: reporte_notas.pdf")
        for e in estudiantes:
            print(f"  {e['nombre']}: {e['nota']}")
        return True
