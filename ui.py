def ui_print(map): #precisamos fazer um laço pois o nosso mapa se trata de uma lista(array)
    for row in map:
        for column in row:
            print(column, end='')

        print("") #quebra de linha



def ui_key():
    return input()


def ui_msg_lost():
    print("Pacman Morreu!")


def ui_msg_win():
    print("Você ganhou o game !")