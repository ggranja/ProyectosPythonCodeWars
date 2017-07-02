import unittest
from ProyectosPythonCodeWars import *
from Clases import Player

class Test_test1(unittest.TestCase):
    def test_duck_duck_goose(self):
        players=[Player("Pepe"),Player("Ana"),Player("Felipe")]
        self.assertEquals(duck_duck_goose(players, 1), "Pepe")
        self.assertEquals(duck_duck_goose(players, 3), "Felipe")
        self.assertEquals(duck_duck_goose(players, 2), "Ana")    

    def test_welcome(self):
        self.assertEquals(greet('english'), 'Welcome')
        self.assertEquals(greet('dutch'), 'Welkom')
        self.assertEquals(greet('IP_ADDRESS_INVALID'), 'Welcome')
        self.assertEquals(greet(''), 'Welcome')
        self.assertEquals(greet(2), 'Welcome')

if __name__ == '__main__':
    unittest.main()
