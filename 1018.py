N = int(input())
print(N)
NOTAS100 = N // 100
N = N % 100
NOTAS50 = N // 50
N = N % 50
NOTAS20 = N // 20
N = N % 20
NOTAS10 = N // 10
N = N % 10
NOTAS5 = N // 5
N = N % 5
NOTAS2 = N // 2
N = N % 2
NOTAS1 = N // 1


print(f"{NOTAS100} nota(s) de R$ 100,00")
print(f"{NOTAS50} nota(s) de R$ 50,00")
print(f"{NOTAS20} nota(s) de R$ 20,00")
print(f"{NOTAS10} nota(s) de R$ 10,00")
print(f"{NOTAS5} nota(s) de R$ 5,00")
print(f"{NOTAS2} nota(s) de R$ 2,00")
print(f"{NOTAS1} nota(s) de R$ 1,00")