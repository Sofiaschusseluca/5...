nota=float(input("ingrese la nota del examen: "))
if nota >= 0 and nota <= 5:
    print("Desaprobado")
elif nota >= 6 and nota <= 8:
    print("Aprobado")
elif nota >= 9 and nota <= 10:
    print("Excelente")