v1 = float(input("ingrese el primer valor: "))
v2 = float(input("ingrese el segundo valor: "))
op = input("ingrese operacion (+, -, *, /): ")
if op == "+":
    print("Resultado:", v1 + v2)
elif op == "-":
    print("Resultado:", v1 - v2)
elif op == "*":
    print("Resultado:", v1 * v2)
elif op == "/":
    if v2 != 0:
        print("Resultado:", v1 / v2)
    else:
        print("no se puede dividir por cero")