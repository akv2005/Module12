import unittest
import runner

class RunnerTest(unittest.TestCase):

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

    def test_challenge(self):
        Vasya = runner.Runner('Вася')
        Olya = runner.Runner('Оля')
        for _ in range(10):
            Vasya .walk()
            Olya.run()
        self.assertNotEqual(Vasya.distance, Olya.distance)

if __name__ == "__main":
    unittest.main