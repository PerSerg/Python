
maps = [1,2,3,
        4,5,6,
        7,8,9]


win_lines = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]


def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])


def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol


def get_result():
    win = ""

    for i in win_lines:
        if maps[i[0]] == "X" and maps [i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps [i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win

        
player1 = True
GameOver = False

while GameOver == False:

    print_maps()

    if player1 == True:
        symbol = "X"
        step = int(input("Чел ходит: "))
    else:
        symbol = "O"
        step = int(input("Чувак ходит: "))

    step_maps(step, symbol)
    win = get_result()
    if win !="":
        GameOver = True
    else:
        GameOver = False

    player1 = not(player1)


print_maps()
print("WIN", win)
