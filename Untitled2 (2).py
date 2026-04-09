#PEDIR LA EDAD
edad= int(input("ingrese la edad: "))
if edad >= 0 and edad<12:
    print("es un Niño")
elif edad >13 and edad<17:
    print("es un Adolescente")
elif edad>18 and edad<64:
    print("es un Adulto")
else:
    print :("es un adulto mayor")
