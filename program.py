from ui import ui_print
from Init import play
from ui import ui_key
from ui import ui_msg_lost
from ui import ui_msg_win
from Init import move_ghosts
# @ -> meu personagem
# G -> ghosts
# P -> pilulas/powerup
# . -> espaço vazio
# | and - -> paredes
# Y COLUNA
# X LINHA

map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G...@.|.|",
    "|........|",
    "|--------|"
]

game_finished = False

while not game_finished:

    ui_print(map)
    key =  ui_key()
    valid_key, pacman_alive, won = play(map, key)


    move_ghosts(map)

    if not pacman_alive:
        ui_msg_lost()
        #print("Pacman Morreu!")
        game_finished = True

    elif won:
        ui_msg_win()
        #print("Você ganhou o game !") #voce ganha apos coletar duas pilulass
        game_finished = True