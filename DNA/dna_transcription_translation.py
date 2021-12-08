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


def peptides_reading(peptides_dict: dict, peptides_partition: list) -> str:
    polypeptide_for_peptide = ""
    for peptide in peptides_partition:
        if peptide == "stop":
            polypeptide_for_peptide += "-"
        else:
            polypeptide_for_peptide += peptides_dict[peptide]

    return polypeptide_for_peptide


def polypeptide_translation(dna_sequence: str) -> list:
    peptides_dict = load_data('peptides.json')

    polypeptides = []
    peptides = rna_codons_reading(dna_sequence)
    for peptides_partition in peptides:
        polypeptides.append(peptides_reading(peptides_dict, peptides_partition))

    return polypeptides


def validate_peptides(dna_sequence: str) -> list:
    valid_polypeptides = []

    polypeptides = polypeptide_translation(dna_sequence)
    for polypeptide in polypeptides:
        if "M" in polypeptide:
            start = polypeptide.index("M")
        else:
            continue

        if "-" not in polypeptide or start > polypeptide.index("-"):
            valid_polypeptides.append(polypeptide[start:])
        else:
            valid_polypeptides.append(polypeptide[start:polypeptide.index("-")])

    return valid_polypeptides
