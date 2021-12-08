import json


def dna_and_antisense_sequences(dna_sequence: str) -> (str, str):
    pattern = {"A": "T", "T": "A", "C": "G", "G": "C"}

    return dna_sequence, change_pattern(dna_sequence, pattern)


def rna_transcription(dna_sequences: (str, str)) -> (str, str):
    pattern = {"A": "U", "T": "A", "C": "G", "G": "C"}

    return change_pattern(dna_sequences[0], pattern), change_pattern(dna_sequences[1], pattern)


def change_pattern(sequence: str, pattern: dict) -> str:
    complement_sequence = []
    for element in sequence[::-1]:
        complement_sequence.append(pattern[element])

    return "".join(complement_sequence)


def split_in_threesomes(sequence: str) -> list:
    partitions = []
    for i in range(0, len(sequence), 3):
        partition = sequence[i: i + 3]

        if len(partition) == 3:
            partitions.append(partition)

    return partitions


def rna_threesomes(dna_sequence: str) -> list:
    threesomes = []
    rna_sequences = rna_transcription(dna_and_antisense_sequences(dna_sequence))
    for i in range(2):
        for sub_sequence in [rna_sequences[i], rna_sequences[i][2:], rna_sequences[i][1:]]:
            threesomes.append(split_in_threesomes(sub_sequence))

    return threesomes


def load_data(file: str):
    with open(file) as json_file:
        data = json.load(json_file)

    return data


def rna_threesomes_to_threesomes_peptides(codons_data: dict, rna_threesomes_list: list) -> list:
    threesomes_peptides = []
    for threesome in rna_threesomes_list:
        threesomes_peptides.append(codons_data[threesome].lower())

    return threesomes_peptides


def rna_codons_reading(dna_sequence: str) -> list:
    codons_dict = load_data('codons.json')
    peptides = []

    codons = rna_threesomes(dna_sequence)

    for codons_partition in codons:
        peptides_for_codons_partition = rna_threesomes_to_threesomes_peptides(codons_dict, codons_partition)
        peptides.append(peptides_for_codons_partition)

    return peptides

    return codons


def polypeptide_translation(dna_sequence: str) -> list:
    with open('peptides.json') as json_file:
        peptides = json.load(json_file)

    polypeptides = []
    codons = rna_codons_reading(dna_sequence)
    for codons_set in codons:
        polypeptide_for_codon = ""
        for codon in codons_set:
            if codon != "stop":
                polypeptide_for_codon += peptides[codon]
            else:
                polypeptide_for_codon += "-"

        polypeptides.append(polypeptide_for_codon)

    return polypeptides


def validate_peptides(dna_sequence: str) -> list:
    proteins = []

    peptides = polypeptide_translation(dna_sequence)
    for peptide in peptides:
        possible_protein = ""
        for i in peptide:
            if i == "M":
                possible_protein += i
            elif "M" in possible_protein and i != "-":
                possible_protein += i
            elif i == "-":
                proteins.append(possible_protein)
                break
            else:
                break

    return proteins
