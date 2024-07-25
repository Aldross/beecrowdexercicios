codigo1, peca1, valor_unit1 = input().split()
codigo2, peca2, valor_unit2 = input().split()
peca1 = int(peca1)
valor_unit1 = float(valor_unit1)
peca2 = int(peca2)
valor_unit2 = float(valor_unit2)

VALOR = (peca1 * valor_unit1) + (peca2 * valor_unit2)

print(F"VALOR A PAGAR: R$ {VALOR:.2f}")