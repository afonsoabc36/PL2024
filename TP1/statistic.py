import sys

file_path = 'emd.csv'

modalidades = []
aptos = 0
nAptos = 0
ageGroups = {}

next(sys.stdin) # Ignorar o cabeçalho

for line in sys.stdin:
    line = line.strip()
    data = line.split(',')

    idade = int(data[5])
    modalidade = data[8]
    if modalidade not in modalidades:
        modalidades.append(modalidade)
    if data[12] == "true":
        aptos += 1
    else:
        nAptos += 1
    ageRounded = (idade // 5) * 5 # Arredonda para o múltiplo de 5 inferior
    ageGroup = f"[{ageRounded}-{ageRounded+4}]"
    ageGroups.setdefault(ageGroup, 0)
    ageGroups[ageGroup] += 1

# Resultados
print("\n----------------Estatísticas----------------\n")

print("Lista ordenada alfabeticamente das modalidades desportivas:")
for modalidade in sorted(modalidades):
    print(f"\t{modalidade}")

print ("\n=====================================\n")

print("Percentagem de atletas aptos e inaptos para a prática desportiva:")
totalAtletas = aptos + nAptos
print(f"\tAptos: {(aptos/totalAtletas * 100):.0f}%")
print(f"\tInaptos: {(nAptos/totalAtletas * 100):.0f}%")

print ("\n=====================================\n")

print("Distribuição de atletas por escalão etário:")
for ageGroup, count in sorted(ageGroups.items()):
    if count == 1:
        print(f"\t{ageGroup}: {count} atleta")
    elif count != 0:
        print(f"\t{ageGroup}: {count} atletas")
