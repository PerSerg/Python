a = int(input())

if a == 100:
    print("число равно 100")
elif a > 100:
    print("число больше 100")
elif a == 50:
    print("число равно 50")
elif a < 100 and a > 50:
    print("число больше 50, но меньше 100")
else:
    print("число меньше 50")