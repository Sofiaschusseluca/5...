v1 = float(input("ingrese el importe de la compra: "))
if v1 > 50000:
    final = v1 * 0.70  # Aplica 30% de descuento
elif v1 > 20000:
    final = v1 * 0.80  # Aplica 20% de descuento
elif v1 > 10000:
    final = v1 * 0.90  # Aplica 10% de descuento
else:
    final = v1
print("El precio final con descuento es:", final)