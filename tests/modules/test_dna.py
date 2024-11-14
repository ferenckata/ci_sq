'''Test class '''
import unittest
from cisq.modules.dna import DNA


class TestDNA(unittest.TestCase):
    """ Testing DNA class functionalities """

    def test_rev_comp(self):
        """ Testing that DNA is correctly reverse complemented """
        dna_in = "AATTG"
        expected_revcomp = "CAATT"
        dna_class = DNA()
        actual_revcomp = dna_class.rev_comp(dna_in)
        self.assertEqual(expected_revcomp, actual_revcomp)
