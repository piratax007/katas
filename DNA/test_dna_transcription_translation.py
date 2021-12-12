from unittest import TestCase
import dna_transcription_translation as dnatt

class Test(TestCase):
    def test_dna_and_antisense_sequences(self):
        self.assertEqual(dnatt.dna_and_antisense_sequences("A"), ("A", "T"),
                         "The output must be a two single DNA nucleotides")
        self.assertEqual(dnatt.dna_and_antisense_sequences(""), ("", ""),
                         "For an empty input, the output must be an empty tuple")
        self.assertEqual(dnatt.dna_and_antisense_sequences("AGCTAC"), ("AGCTAC", "GTAGCT"),
                         "The output must be the adn_sequence and his antisense")
        self.assertEqual(dnatt.dna_and_antisense_sequences("CATGCCCTAA"), ("CATGCCCTAA", "TTAGGGCATG"),
                         "The output must be the adn_sequence and his antisense")

    def test_rna_transcription(self):
        self.assertEqual(dnatt.rna_transcription(dnatt.dna_and_antisense_sequences("A")), ("U", "A"),
                         "The output must be a two single RNA nucleotides")
        self.assertEqual(dnatt.rna_transcription(dnatt.dna_and_antisense_sequences("")), ("", ""),
                         "For an empty input, the output must be an empty tuple")
        self.assertEqual(dnatt.rna_transcription(dnatt.dna_and_antisense_sequences("CATGCCCTAA")),
                         ("UUAGGGCAUG", "CAUGCCCUAA"), "The output must be a tuple of two RNA sequences")

    def test_split_in_threesomes(self):
        self.assertEqual(dnatt.split_in_threesomes("A"), [], "If the input has lesser than three nucleotides, the"
                                                             "output is an empty list")
        self.assertEqual(dnatt.split_in_threesomes(""), [], "An empty input result in an empty output list")
        self.assertEqual(dnatt.split_in_threesomes("CAUGCCCUAA"),
                         ["CAU", "GCC", "CUA"], "Return a list with corresponding threesomes")

    def test_rna_threesomes(self):
        self.assertEqual(dnatt.rna_threesomes("CATGCCCTAA"),
                         [["UUA", "GGG", "CAU"], ["AGG", "GCA"], ["UAG", "GGC", "AUG"], ["CAU", "GCC", "CUA"],
                          ["UGC", "CCU"], ["AUG", "CCC", "UAA"]], "")

    def test_rna_codons_reading(self):
        self.assertEqual(dnatt.rna_codons_reading("CATGCCCTAA"),
                         [["leu", "gly", "his"], ["arg", "ala"], ["stop", "gly", "met"],  ["his", "ala", "leu"],
                          ["cys", "pro"], ["met", "pro", "stop"]], "")

    def test_polypeptide_translation(self):
        self.assertEqual(dnatt.polypeptide_translation("CATGCCCTAA"), ["LGH", "RA", "-GM", "HAL", "CP", "MP-"], "")

    def test_validate_peptides(self):
        self.assertEqual(dnatt.validate_peptides("CATGCCCTAA"), ["M", "MP"], "")