import json


def dna_and_antisense_sequences(dna_sequence: str) -> (str, str):
    pattern = {"A": "T", "T": "A", "C": "G", "G": "C"}

    return dna_sequence, change_pattern(dna_sequence, pattern)


def rna_transcription(dna_sequences: (str, str)) -> (str, str):
    pattern = {"A": "U", "T": "A", "C": "G", "G": "C"}

    return change_pattern(dna_sequences[0], pattern), change_pattern(dna_sequences[1], pattern)


def change_pattern(sequence: str, pattern: dict) -> str:
    temporal_sequence = []
    for element in sequence[::-1]:
        temporal_sequence.append(pattern[element])

    return "".join(temporal_sequence)


def split_in_sets_of_length_3(sequence: str) -> list:
    partitions = []
    for i in range(0, len(sequence), 3):
        partition = sequence[i: i+3]

        if len(partition) == 3:
            partitions.append(partition)

    return partitions


def rna_sets(dna_sequence: str) -> list:
    _sets = []
    rna_sequences = rna_transcription(dna_and_antisense_sequences(dna_sequence))
    for i in range(2):
        for sub_sequence in [rna_sequences[i], rna_sequences[i][2:], rna_sequences[i][1:]]:
            _sets.append(split_in_sets_of_length_3(sub_sequence))

    return _sets


def rna_codons_reading(dna_sequence: str) -> list:
    with open('codons.json') as json_file:
        sets = json.load(json_file)

    codons = []
    rna_partitions = rna_sets(dna_sequence)
    for partition in rna_partitions:
        codons_for_partition = []
        for sub_partition in partition:
            codons_for_partition.append(sets[sub_partition].lower())

        codons.append(codons_for_partition)

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
