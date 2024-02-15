# TP1 : Análise de um dataset

## Compilar:
        python3 statistic.py < emd.csv

## Objetivos:
Ler o dataset, processá-lo e criar os seguintes resultados:
- Lista ordenada alfabeticamente das modalidades desportivas;
- Percentagens de atletas aptos e inaptos para a prática desportiva;
- Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...
  
**Nota**: É **proibido** usar o módulo csv.

## Resumo:
O programa **lê do *stdin*** linha a linha as informações contidas no ficheiro passado como parâmetro (ignoranda a primeira linha) e, para cada uma, recolhe a informação do atleta sobre a modalidade que pratica, o resultado do exame médico desportivo (EMD) e a idade.
A modalidade é inserida numa lista de modalidades (caso não se encontre na mesma), é incrementado o número de atletas aptos/inaptos consoante o resultado obtido no EMD e incrementado também o número de atletas do escalão etário onde se insere o atleta.
Após ser detetado o EOF, são expostas as estatísticas do ficheiro, enumerando os resultados obtidos aos 3 pontos presentes nos objetivos deste trabalho.

## Resultado:

### Lista ordenada alfabeticamente das modalidades desportivas:
        Andebol
        Atletismo
        BTT
        Badminton
        Basquetebol
        Ciclismo
        Dança
        Equitação
        Esgrima
        Futebol
        Karaté
        Orientação
        Parapente
        Patinagem
        Triatlo

**=====================================================================**

### Percentagem de atletas aptos e inaptos para a prática desportiva:
        Aptos: 54%
        Inaptos: 46%

**=====================================================================**

### Distribuição de atletas por escalão etário:
        [20-24]: 80 atletas
        [25-29]: 102 atletas
        [30-34]: 104 atletas
        [35-39]: 14 atletas