valor = float(input())

if 0 <= valor <= 25.0000:
    print("Intervalo [0,25]")
elif 25.0001 <= valor <= 50.0000:
    print("Intervalo (25,50]")
elif 50.0001 <= valor <= 75.0000:
    print("Intervalo (50,75]")
elif 75.0001 <= valor <= 100.0000:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")