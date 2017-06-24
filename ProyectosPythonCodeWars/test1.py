import unittest
from ProyectosPythonCodeWars import duck_duck_goose
from Clases import Player

class Test_test1(unittest.TestCase):
    def test_duck_duck_goose(self):
        players=[Player("Pepe"),Player("Ana"),Player("Felipe")]
        self.assertEquals(duck_duck_goose(players, 1), "Pepe")
        self.assertEquals(duck_duck_goose(players, 3), "Felipe")
        self.assertEquals(duck_duck_goose(players, 2), "Ana")    


if __name__ == '__main__':
    unittest.main()
