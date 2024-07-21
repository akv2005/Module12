import unittest
import runner1


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.result = {}
        self.all_results = {}

    def setUp(self):
        self.usein = runner1.Runner('Усэйн', 10)
        self.anrey = runner1.Runner('Андрей', 9)
        self.nic = runner1.Runner('Ник', 3)

    @classmethod
    def tearDownClass(self):
        for key in self.all_results:
            print(self.all_results[key])


    def test_run1(self):
        self.result = runner1.Tournament(90, self.usein, self.nic)
        self.all_results[1] = self.result.start()
        self.assertTrue(self.usein,self.nic)

    def test_run2(self):
        self.result = runner1.Tournament(90, self.nic, self.anrey)
        self.all_results[2] = self.result.start()
        self.assertTrue(self.anrey, self.nic)

    def test_run3(self):
        self.result = runner1.Tournament(90, self.anrey, self.usein, self.nic)
        self.all_results[3] = self.result.start()
        self.assertTrue(self.usein, self.nic)



if __name__ == "__main":
    unittest.main()
