# a = [1,2,3]
# b = [3,2,1]
# for i in a:
#     for j in b:
#         print(i, j)

# for i in range(1, 2):
#     for j in range(1,11):
#         if i == j:
#             continue
#         print(i, "Х", j, "=", i*j)

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

def print_map():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])


def step_map(step, symbol):
    inm = maps.index(step)
    maps[inm]

def get_res():
    win = ""

    for i in win_lines:
        if maps[i[0]] == "X" and maps [i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps [i[1]] == "O" and maps[i[2]] == "O":
            win = "O"
        
player1 = True
GameOver = False

while GameOver == False:
    print_map()

    if player1 == True:
        symbol = "X"
        step = int(input("Чел ходит: "))
    else:
        symbol = "O"
        step = int(input("Чувак ходит: "))
    step_map(step, symbol)
    win = get_res()

    if win !="":
        GameOver = True
    else:
        GameOver = False

    player1 = not(player1)

print_map()
print("WIN", win)