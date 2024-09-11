import unittest
from Runner import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.part_1 = Runner('Усэйн', speed=10)
        self.part_2 = Runner('Андрей', speed=9)
        self.part_3 = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    def test_run_1(self):
        self.tournament_1 = Tournament(90, self.part_1, self.part_3)  #создаем объект класса Забег

        self.all_results = self.tournament_1.start()  # в словарь all_result записываем результат функции (место:участн)

        last_runner_name = self.all_results[max(self.all_results.keys())].name  # записываем имя с максимальным местом
        self.assertTrue(last_runner_name == 'Ник')  # вызываем юнит-метод сравнения

        TournamentTest.all_results[1] = self.all_results  # записываем словарь с ключом 1

    def test_run_2(self):
        self.tournament_2 = Tournament(90, self.part_2, self.part_3)  # создаем объект класса Забег

        self.all_results = self.tournament_2.start()  # в словарь all_result записываем результат функции (место:участн)

        last_runner_name = self.all_results[max(self.all_results.keys())].name  # записываем имя с максимальным местом
        self.assertTrue(last_runner_name == 'Ник')  # вызываем юнит-метод сравнения

        TournamentTest.all_results[2] = self.all_results  # записываем словарь с ключом 2


    def test_run_3(self):
        self.tournament_3 = Tournament(90, self.part_1, self.part_2, self.part_3)  # создаем объект класса Забег

        self.all_results = self.tournament_3.start()  # в словарь all_result записываем результат функции (место:участн)

        last_runner_name = self.all_results[max(self.all_results.keys())].name  # записываем имя с максимальным местом
        self.assertTrue(last_runner_name == 'Ник')  # вызываем юнит-метод сравнения

        TournamentTest.all_results[3] = self.all_results  # записываем словарь с ключом 3


if __name__ == "__main__":
    unittest.main()
