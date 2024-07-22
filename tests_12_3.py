import unittest
import runner
import runner1

class RunnerTest(unittest.TestCase):
    is_frozen = True

    def test_walk(self):
        ocr = runner.Runner('Вася')
        for _ in range(10):
            ocr.walk()
        self.assertEqual(ocr.distance, 50)

    def test_run(self):
        ocr = runner.Runner('Вася')
        for _ in range(10):
            ocr.run()
        self.assertEqual(ocr.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        Vasya = runner.Runner('Вася')
        Olya = runner.Runner('Оля')
        for _ in range(10):
            Vasya.walk()
            Olya.run()
        self.assertNotEqual(Vasya.distance, Olya.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = False

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

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
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
    unittest.main
