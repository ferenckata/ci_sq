''' dna class '''
from Bio.Seq import Seq


class DNA:
    """ This class will do reverse complementing"""

    def rev_comp(self, sequence: str) -> str:
        """ Do the reverse complement of a sequence """
        my_dna = Seq(sequence)
        return my_dna.reverse_complement()
