estudiantes = [
    ("Carlos", 4.5),
    ("María", 2.8),
    ("Juan", 3.2),
    ("Ana", 1.9),
    ("Luis", 3.0),
    ("Sofia", 4.8),
]

# Recorrer cada estudiante
for nombre, nota in estudiantes:
    print(f"\nEstudiante: {nombre} | Nota: {nota}")
    
    if nota > 3.0:
        print("🎉 ¡Felicitaciones, aprobaste!")
    else:
        print("❌ Curso fallido.")