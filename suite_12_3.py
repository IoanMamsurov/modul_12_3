import unittest
import n_1
import modul_12_1

n_1TS = unittest.TestSuite()
n_1TS.addTest(unittest.TestLoader().loadTestsFromTestCase(n_1.TournamentTest))
n_1TS.addTest(unittest.TestLoader().loadTestsFromTestCase(modul_12_1.TestRunner))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(n_1TS)