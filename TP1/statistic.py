import os

os.chdir("./")
file_path = 'emd.csv'

idades = []
modalidades = []
aptos = 0
nAptos = 0
firstLine = True

if os.path.exists(file_path):
    
    with open(file_path, 'r') as file:
        for line in file:
            if firstLine:
                firstLine = False
                continue
            line = line.strip()
            data = line.split(',')

            idades.append(data[5])
            modalidade = data[8]
            if modalidade not in modalidades:
                modalidades.append(modalidade)
            if data[12] == "true":
                aptos += 1
            else:
                nAptos += 1
else:
    print(f"The file {file_path} does not exist.")

print("\n----------------Estatísticas----------------\n")
print("Lista ordenada alfabeticamente das modalidades desportivas:")
for modalidade in sorted(modalidades):
    print(f"\t{modalidade}")

print ("\n=====================================\n")

print("Percentagem de atletas aptos e inaptos para a prática desportiva:")
totalAtletas = aptos + nAptos
print(f"Aptos: {(aptos/totalAtletas * 100):.0f}%")
print(f"Não aptos: {(nAptos/totalAtletas * 100):.0f}%")


