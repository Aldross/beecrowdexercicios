A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

delta = (B ** 2) - (4 * A * C)

try:
    if delta < 0:
        print(f"Impossivel calcular")
    else:
        R1 = (-B + ((delta) ** 0.5)) / (2 * A)
        R2 = (-B - ((delta) ** 0.5)) / (2 * A)
        print(f"R1 = {R1:.5f}")
        print(f"R2 = {R2:.5f}")
except (ZeroDivisionError, ValueError):
    print(f"Impossivel calcular")
