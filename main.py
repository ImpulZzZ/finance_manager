from PyQt5.QtWidgets import *
from gui import welcome


def main():

    app = QApplication([])
    MainWindow = QMainWindow()
    ui = welcome.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

if __name__ == '__main__':
    main()
