# Создайте программу для игры в ""Крестики-нолики"".


field_game = [1,2,3,4,5,6,7,8,9] # Игровое поле
victories = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] # Победные варианты
 

def print_field():   # Вывод поля на экран
    print(*field_game[:3])
    print(*field_game[3:6])
    print(*field_game[6:])
 
 
def step_field(step,symbol):  # Сделать ход в ячейку
    ind = field_game.index(step)
    field_game[ind] = symbol
 

def get_result():  # Проверка на победителя
    victory = "" 
    for i in victories:
        if field_game[i[0]] == field_game[i[1]] == field_game[i[2]] == "X":
            victory = "X"
        if field_game[i[0]] == field_game[i[1]] == field_game[i[2]] == "O":
            victory = "O"              
    return victory
 
game_over = False
player1 = True
 
while game_over == False:
    print_field()
    if player1 == True:
        symbol = "X"
        step = int(input("Куда ставить Х?: "))
    else:
        symbol = "O"
        step = int(input("Куда ставить О?: "))
    step_field(step,symbol)
    victory = get_result()
    if victory != "":
        game_over = True
    else:
        game_over = False
 
    player1 = not(player1)        
         
print_field()
print("Победили", victory)


