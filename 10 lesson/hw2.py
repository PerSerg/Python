class Stydent:
    name = " "
    number = 0
    age = 0
    NewAge = " "
    NewNumber = " "
    def forename(self):
        print("Имя студента ", self.name)
    def year(self):
        print("Возраст студента ", self.age)  
    def numb(self):
        print("Номер студента ", self.number)
    def NA(self):
        print("Если возраст изменился, то введите новые данные", self.NewAge)
    def NA(self):
        print("Если номер студента изменился, то введите новые данные", self.NewNumber)


Stydent1 = Stydent()
Stydent1.name = "Иван"
Stydent1.age = 21
Stydent1.number = 3
Stydent1.forename()
Stydent1.year()
Stydent1.numb()


Stydent2 = Stydent()
Stydent2.name = "Пётр"
Stydent2.age = 22
Stydent2.number = 1
Stydent2.forename()
Stydent2.year()
Stydent2.numb()


Stydent3 = Stydent()
Stydent3.name = "Фёдор"
Stydent3.age = 22
Stydent3.number = 2
Stydent3.forename()
Stydent3.year()
Stydent3.numb()


print(f"{Stydent1.name}у {Stydent1.age } год(а) порядковый номер в списке {Stydent1.number}")
print(f"{Stydent2.name}у {Stydent2.age } год(а) порядковый номер в списке {Stydent2.number}")
print(f"{Stydent3.name}у {Stydent3.age } год(а) порядковый номер в списке {Stydent3.number}")


    