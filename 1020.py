TEMPO = int(input())

ANO = TEMPO // 365
TEMPO = TEMPO % 365
MES = TEMPO // 30
TEMPO = TEMPO % 30
DIA = TEMPO

print(f"{ANO} ano(s)")
print(f"{MES} mes(es)")
print(f"{DIA} dia(s)") 