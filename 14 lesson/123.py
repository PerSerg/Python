# class Animal:
#     def eat(self):
#         print("ЖРААААТЬ!!!")

#     def sleep(self):
#         print("Хрр..")


# class Cat(Animal):
#     def destroy(self):
#         print("Кот крушить, кот ломать!")

# class Dog(Animal):
#     def happy(self):
#         print("Щас уссусь от счастья!")

# cat1 = Cat()
# cat1.eat()
# cat1.destroy()

# dog1 = Dog()
# dog1.sleep()
# dog1.happy()

# __________________________________________________________________________

# class Car():
#     def __init__(self):
#         self.__maxprice = 1500

#     def sell(self):
#         print(format(self.__maxprice))
#     def setMaxPrice(self, price):
#         self.__maxprice = price

# c = Car()
# c.sell()

# c.__maxprice = 999
# c.sell()

# c.setMaxPrice(999)
# c.sell()

# __________________________________________________________________________

# class Move():
#     def render(self):
#         print("render")

# class Films(Move):
#     def render(self):
#         print("render films")

# class Anime(Move):
#     def render(self):
#         print("render anime")

# f1 = Films()
# f1.render()

# a1 = Anime()
# a1.render()

# __________________________________________________________________________

class Human:
    def __init__(self, name):
        self.name = name

    def ans(self, question):
        print("Вопрос:")

    def __str__(self):
        return f'{self.name}'
    
class Erik(Human):
    def ask(self, someone, question):
        print(f'{someone}, {question}')
        someone.ans(question)
        print()

super