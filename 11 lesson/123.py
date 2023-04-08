# # import PyQt5
# import sys
# # Модуль предоставляющий доступ к переменным и функциям связанным с интерпретатором
# from PyQt5.QtWidgets import QApplication, QWidget
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = QWidget()
#     w.resize(350, 350)
#     w.setWindowTitle("Hello world")
#     w.show()
#     sys.exit(app.exec_())


    # QT - объеденяет все классы и модули
    # QTcore - содержит в себе неграфические классы
    # QT gui - содержит компоненты графического интерфейса, рассширяет предыдущий модуль
    # QTWidgets - содержит большинство виджетов из PyQT5
    # QTnetwork позволяет создавать классы с сетевым програмированием
    # QTmultimedia - низкоуовневая мультимедийная функционалность
    # QT SQL - реализует интеграцию с базами данных

# Виджеты:
# QlineEdit - поле ввода данных
# QradioButton - кружочек, который отмечают для ввода варианта ответа
# QcomboBox - выпадающее меню
# QcheckBox - квадратик для галочки
# QmenuBar - горизонтальная строка меню
# QtoolBar - опциаональные панели на строке меню
# Qtab разбить содержимое страницы
# QscroolBar - создание полос прокрутки
# Qsplitter - разделители
# Qdock - подокно
# * - всё! (для импорта)

# QboXLayout - линейное окно
# hbox = QHBoxLayout(w) - горизонтальное окно с кнопками
# hbox = QVBoxLayout(w) - вертикальное окно с кнопками
# QGridLayout - окно сеткой


# import sys
# from PyQt5.QtWidgets import *

# if __name__ == "__main__":
#     app = QApplication([])
#     w = QWidget()
#     w.setWindowTitle("QboxLayout")
#     btn1 = QPushButton("Bird")
#     btn2 = QPushButton("Animal")
#     btn3 = QPushButton("Fish")

#     hbox = QVBoxLayout(w)

#     hbox.addWidget(btn1)
#     hbox.addWidget(btn2)
#     hbox.addWidget(btn3)

#     w.show()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import *

# if __name__ == "__main__":
#     app = QApplication([])
#     w = QWidget()
#     grid = QGridLayout(w)

#     for i in range(3):
#         for j in range(3):
#             grid.addWidget(QPushButton("button"), i, j)
#     w.show()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QPalette


# if __name__ == "__main__":
#     app = QApplication([])
#     app.setStyle("Fusion") # тема оформления
    
#     qp = QPalette()
#     qp.setColor(QPalette.ButtonText, Qt.yellow) # цвет текста на кнопке
#     qp.setColor(QPalette.Button, Qt.black) # цвет кнопки
#     qp.setColor(QPalette.Window, Qt.black) # цвет окна
#     app.setPalette(qp)
                
#     w = QWidget()
#     grid = QGridLayout(w)

#     for i in range(3):
#         for j in range(3):
#             grid.addWidget(QPushButton("button"), i, j)
#     w.show()
#     sys.exit(app.exec_())


# import numpy as np # сокращение

# x = [1, 2, 3, 4, 5]
# y = [a + 2 for a in x]
# print(y)


# n1 = np.array([1, 2, 3, 4, 5])
# n2 = n1+2
# print(n2)


import numpy as np
import matplotlib.pyplot as plt

a = np.arange(50)
b = np.random.randint(0, 10, size=(3, a.size))
y = 1333 + a

fig, ax = plt.subplots(figsize=(5, 3))
ax.stackplot(y, a+b, labels=["ERIK", "ALEX", "DOC"])
ax.set_title("TOP GUN")
ax.legend(loc="upper left")
ax.set_ylabel("total debt")
ax.set_xlim(xmin=y[0], xmax=y[-1])
fig.tight_layout()
plt.show()