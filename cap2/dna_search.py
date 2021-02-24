from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # Códon é uma tupla de 3 Nucleotides
Gene = List[Codon]  # Gene é uma lista de códons

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


# Percorre a string fornecida e converte os 3 próximos caracteres em Codons,
# a serem adicionados ao final de um novo Gene
def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)
    return gene


my_gene: Gene = string_to_gene(gene_str)


#  Função ilustrativa, pois list, tuple e range implementam o método __contains__(), com operador in
#  Ex.: print(acg in my_gene)

def linear_contains(gene: Gene, key_codon: Codon) -> bool:  # Busca linear
    for codon in gene:
        if codon == key_codon:
            return True
    return False


acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
print(linear_contains(my_gene, acg))  # True
print(linear_contains(my_gene, gat))  # False


def binary_contains(gene: Gene, key_codon: Codon) -> bool:  # Busca binária
    low: int = 0                # Intervalo que
    high: int = len(gene) - 1   # engloba toda a lista
    while low <= high:  # ainda há espaço para pesquisar
        mid: int = (low + high) // 2  # calcula o meio, através da divisão inteira
        if gene[mid] < key_codon:  # Se o elemento procurado for maior que o meio do intervalo
            low = mid + 1          # desloca o menor elemento para a direita da lista
        elif gene[mid] > key_codon:  # Se o elemento procurado for maior que o meio do intervalo
            high = mid - 1           # desloca o menor elemento para a esquerda da lista
        else:
            return True
    return False

# Busca binária também pode ser implementada pelo módulo bisect da biblioteca padrão do Python


my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg))  # True
print(binary_contains(my_sorted_gene, gat))  # False

