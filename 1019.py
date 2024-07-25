N = int(input())

HORA = N // 3600
N = N % 3600
MINUTO = N // 60
N = N % 60
SEGUNDO = N

print(f"{HORA}:{MINUTO}:{SEGUNDO}")