""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""

import os
import matplotlib.pyplot as plt


def analyze_line_dna(string: str):
    if string.startswith('>'):
        genes.append({'gene': string[1:], 'dna': ''})
    else:
        genes[-1]['dna'] += string


def translate_from_dna_to_rna(dna: str) -> str:
    rna = dna.replace('T', 'U')
    return rna


def count_nucleotides(dna: str) -> dict:
    num_of_nucleotides = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in num_of_nucleotides.keys():
        num_of_nucleotides[nucleotide] = dna.count(nucleotide)
    return num_of_nucleotides


def translate_rna_to_protein(rna: str) -> str:
    valid_rna = rna if len(rna) % 3 == 0 else rna[:-(len(rna) % 3)]
    valid_rna_list = [valid_rna[i:i + 3] for i in range(0, len(valid_rna), 3)]
    protein = ''
    for triplet in valid_rna_list:
        protein += protein_replaces[triplet]
    return protein


def build_genes_plot():
    y_pos = tuple(range(len(genes[0]['stats'])))
    for gene in genes:
        plt.bar(y_pos, [value / sum(gene['stats'].values()) for value in gene['stats'].values()],
                label=gene['gene'], alpha=0.5)
    plt.xticks(y_pos, genes[0]['stats'].keys())
    plt.title('Histograms for nucleotide gene statistics')
    plt.xlabel('Nucleotide name')
    plt.ylabel('Probability density of nucleotide in gene')
    plt.grid(axis='y')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    genes = []
    path = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(path, './files/dna.fasta'), 'r') as file:
        for line in file:
            analyze_line_dna(line.rstrip())
    with open(os.path.join(path, './files/rna_codon_table.txt'), 'r') as file:
        text = file.read().split()
    protein_replaces = dict(zip(text[::2], text[1::2]))

    for gene in genes:
        gene['rna'] = translate_from_dna_to_rna(gene['dna'])
        gene['stats'] = count_nucleotides(gene['dna'])
        gene['protein'] = translate_rna_to_protein(gene['rna'])

    to_write = ('stats', 'rna', 'protein')
    for name in to_write:
        with open(os.path.join(path, f"./files/output_{name}.txt"), 'w') as file:
            for gene in genes:
                file.write(f">{gene['gene']}\n{gene[name]}\n")

    print(genes)
    build_genes_plot()
