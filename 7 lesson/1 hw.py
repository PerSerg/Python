def amount(a,b):
    if a > b:
        a,b = b,a
    c = 0
    for i in range (a, b+1):
        c += i
    print(c)
    
amount(int(input()), int(input()))