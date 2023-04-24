import unittest
from Init import find_pacman, move_pacman

class PacmanTest(unittest.TestCase):
    def test_find_pacman(self):
        map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        x, y = find_pacman(map)

        self.assertEqual(x, 3) #o assertEqual serve para comparar com o valor passado no parametro "3"
        self.assertEqual(y, 5) #o assertEqual serve para comparar com o valor passado no parametro "5"
        #são valores que vieram da saida do programa principal

    def teste_find_pacman_when_pacman_doesnt_exist(self):

        map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G.....|.|",
            "|........|",
            "|--------|"
        ]

        x, y = find_pacman(map)

        self.assertEqual(x, -1)
        self.assertEqual(y, -1)

    def test_move_pacman(self):
        map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        move_pacman(map, 4, 1) #contando a partir do 1, linha 4 coluna 1, um teste para movimentar o pacman @

        new_x, new_y = find_pacman(map)

        self.assertEqual(new_x, 4)
        self.assertEqual(new_y, 1)