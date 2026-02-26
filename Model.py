# Lista de tuplas con (nombre, nota_final)
estudiantes = [
    ("Carlos", 4.5),
    ("María", 2.8),
    ("Juan", 3.2),
    ("Ana", 1.9),
    ("Luis", 3.0),
    ("Sofia", 4.8),
    ("Pedro", 4.4),
    ("Valeria", 5.0),
]

# Recorrer cada estudiante
for nombre, nota in estudiantes:
    print(f"\nEstudiante: {nombre} | Nota: {nota}")

    if nota >= 4.5:
        print("🏆 ¡Felicitaciones, ganaste con méritos!")
    elif nota >= 3.0:
        print("✅ ¡Ganaste el curso!")
    else:
        print("❌ Curso fallido.")