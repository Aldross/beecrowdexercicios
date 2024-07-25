A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

MAIOR = A
if B > MAIOR:
    MAIOR = B
if C > MAIOR:
    MAIOR = C

print(f"{MAIOR} eh o maior")