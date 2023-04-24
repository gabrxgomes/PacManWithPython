from ui import ui_print

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

def find_pacman(map):
    pacman_x = -1 #
    pacman_y = -1


    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '@':
                pacman_x = x
                pacman_y = y

    return pacman_x, pacman_y #NAO E VOID FUNC ENTAO ELA OBRIGATORIAMENTE RETORNA ALGO

x, y = find_pacman(map)
print(x) #TEST
print(y) #TEST

#MAS PODEMOS AUTOMATIZAR OS TESTES, VAMO USAR OUTRA CLASSE PRA ISSO 


#vamos mover
def move_pacman(map, 
                next_pacman_x, next_pacman_y):
    pacman_x, pacman_y = find_pacman(map)
    #aqui nos indica que a posição que o pacman esta ou deveria estar está vazia


    everything_to_the_left = map[pacman_x][0:pacman_y]
    everything_to_the_right = map[pacman_x][pacman_y+1:]
    map[pacman_x] = everything_to_the_left + "." + everything_to_the_right

    #tem um pacman no lugar
    everything_to_the_left = map[next_pacman_x][0:next_pacman_y]
    everything_to_the_right = map[next_pacman_x][next_pacman_y+1:]
    map[next_pacman_x] = everything_to_the_left + "@" + everything_to_the_right

ui_print(map)
move_pacman(map, 3, 6)
ui_print(map)
