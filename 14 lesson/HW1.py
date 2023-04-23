class Communication:
    def war(self):
        print("Ушатаю!")

    def peace(self):
        print("ну ты мужиг!")


class Human(Communication):
    def local(self):
        print("Понаприлетали тут!")

class Alien(Communication):
    def visitor(self):
        print("Простите, сами мы не местные...")


Human1 = Human()
Human1.local()
Human1.war()

Alien1 = Alien()
Alien1.visitor()
Alien1.peace()