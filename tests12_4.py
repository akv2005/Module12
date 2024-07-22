import unittest
import runner3
import logging

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            ocr = runner3.Runner('Вася', -5)
            if ocr.speed <= 0:
                raise ValueError(f'Скорость не может быть отрицательной, сейчас: {ocr.speed}')
            for _ in range(10):
                ocr.walk()
            self.assertEqual(ocr.distance, 50)
            logging.info('"test_run" выполнен успешно')
        except ValueError:
            logging.warning(msg='Скорость не может быть отрицательной,', exc_info=True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            ocr = runner3.Runner(10)
            if not isinstance(ocr.name, str):
                raise TypeError(f'Имя не может быть {type(ocr.name).__name__}')
            for _ in range(10):
                ocr.run()
            self.assertEqual(ocr.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning(msg="Неверный тип данных для имени экземпляра Runner", exc_info=True)


    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        Vasya = runner3.Runner('Вася')
        Olya = runner3.Runner('Оля')
        for _ in range(10):
            Vasya.walk()
            Olya.run()
        self.assertNotEqual(Vasya.distance, Olya.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(self):
        self.result = {}
        self.all_results = {}

    def setUp(self):
        self.usein = runner3.Runner('Усэйн', 10)
        self.anrey = runner3.Runner('Андрей', 9)
        self.nic = runner3.Runner('Ник', 3)


    @classmethod
    def tearDownClass(self):
        for key in self.all_results:
            print(self.all_results[key])

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run1(self):
        self.result = runner3.Tournament(90, self.usein, self.nic)
        self.all_results[1] = self.result.start()
        self.assertTrue(self.usein,self.nic)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        self.result = runner3.Tournament(90, self.nic, self.anrey)
        self.all_results[2] = self.result.start()
        self.assertTrue(self.anrey, self.nic)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run3(self):
        self.result = runner3.Tournament(90, self.anrey, self.usein, self.nic)
        self.all_results[3] = self.result.start()
        self.assertTrue(self.usein, self.nic)



logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')