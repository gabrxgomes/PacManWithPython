#from ui import ui_print
import random
# @ -> meu personagem
# G -> ghosts
# P -> pilulas/powerup
# . -> espaço vazio
# | and - -> paredes
# Y COLUNA
# X LINHA

#map = [
    #"|--------|",
    #"|G..|..G.|",
    #"|...PP...|",
    #"|G...@.|.|",
    #"|........|",
    #"|--------|"
#]

def find_pacman(map):
    pacman_x = -1 
    pacman_y = -1


    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '@':
                pacman_x = x
                pacman_y = y

    return pacman_x, pacman_y #NAO E VOID FUNC ENTAO ELA OBRIGATORIAMENTE RETORNA ALGO

#x, y = find_pacman(map)
#print(x) #TEST
#print(y) #TEST

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


#ui_print(map)
#move_pacman(map, 3, 6)
#ui_print(map)


#A FUNÇÃO PLAY retorna dois booleanos
#o primeiro booleano indica que a tecla clicada é uma tecla(key) valida
#a segunda indica que o pacman está vivo

#se o programa continua perguntando sobre a proxima tecla a se clicada significa que ele está vivo
#caso contrario ele está morto 

#o terceiro retorno booleano indica que o pacman venceu o game

def play(map, key):
   # a --> left
   # d --> right
   # w --> up
   # s --> down

   next_x, next_y = next_position(map, key)

    # if it is a invalid key
   is_an_invalid_key = next_x == -1 and next_y == -1
   if is_an_invalid_key:
        return False, True, False

    # if it is not within borders
   if not within_borders(map, next_x, next_y):
        return False, True, False
   


   #if it is a wall/ e se tiver uma parede
   if is_a_wall(map, next_x, next_y):
       return False, True, False
   
   is_a_ghost = map[next_x][next_y] =='G'
   if is_a_ghost:
       
       #print("You are done, you died!")

       return True, False, False
       

   move_pacman(map, next_x, next_y)


   remaining_pills = total_pills(map)
   if remaining_pills ==  0:
       
        return True, True, True
   
   else:
        return True, True,  False
       
       
   
def is_a_wall(map, next_x, next_y):
    is_a_wall = map[next_x][next_y] == '|' or map[next_x][next_y] == '-'
    return is_a_wall

def is_a_ghost(map, next_x, next_y):
    return map[next_x][next_y] == 'G'
    

def is_a_pill(map, next_x, next_y):
    return map[next_x][next_y] == 'P'
    

def is_pacman(map, next_x, next_y):
    return map[next_x][next_y] == '@'
    

def within_borders(map, next_x, next_y):
    number_of_rows = len(map)
    x_is_valid = 0 <= next_x < number_of_rows

    number_of_columns = len(map[0])
    y_is_valid = 0 <= next_y < number_of_columns
    
    
    return x_is_valid and y_is_valid

def total_pills(map):
    total = 0 #definindo o total de pilulas (PP) pelo mapa
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'P':
                total = total + 1
    return total

def next_position(map, key):

   x, y =  find_pacman(map)

   next_x = -1
   next_y = -1

   if key == 'a':
       next_x = x
       next_y = y - 1
   elif key == 'd':
       next_x = x
       next_y = y + 1
   elif key == 'w':
       next_x = x - 1
       next_y = y
   elif key == 's':
       next_x = x + 1
       next_y = y

   return next_x, next_y
   

#ui_print(map)


#play(map, 'w')
#print("***")
#ui_print(map)

#play(map, 'd')
#print("***")
#ui_print(map)

#play(map, 'd')
#print("***")
#ui_print(map)

def find_ghosts(map):
    all_ghosts = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'G':
                all_ghosts.append([x,y])
    return all_ghosts


def move_ghosts(map):
    all_ghosts = find_ghosts(map)
    for ghost in all_ghosts:
        ghost_x = ghost[0]
        ghost_y = ghost[1]


        possible_directions = [
            [ghost_x, ghost_y + 1],
            [ghost_x, ghost_y - 1],
            [ghost_x - 1, ghost_y],
            [ghost_x + 1, ghost_y] #todas as 4 direções do plano cartesiado onde os fantasmas podem se mexer
        ]

        #selecionar randomicamente um possivel movimento de 0 a 3
        # e pegar o valor de x e y desse movimento aleatorio

        random_number =  random.randint(0, 3)

        next_ghost_x =  possible_directions[random_number][0]
        next_ghost_y =  possible_directions[random_number][1]


        #checando antes da movimentação atual
        if not within_borders(map, next_ghost_x, next_ghost_y):
            continue
        if is_a_wall(map ,next_ghost_x, next_ghost_y):
            continue

        if is_a_ghost(map, next_ghost_x, next_ghost_y):
            continue

        if is_a_pill(map, next_ghost_x, next_ghost_y):
            continue

        if is_pacman(map, next_ghost_x, next_ghost_y):
            return True

        #MOVER O FANTASMA PARA UMA POSIÇÃO ALEATORIA
        everything_to_the_left = map[ghost_x][0:ghost_y]
        everything_to_the_right = map[ghost_x][ghost_y+1:]
        map[ghost_x] = everything_to_the_left + "." + everything_to_the_right

        
        everything_to_the_left = map[next_ghost_x][0:next_ghost_y]
        everything_to_the_right = map[next_ghost_x][next_ghost_y+1:]
        map[next_ghost_x] = everything_to_the_left + "G" + everything_to_the_right

        return False