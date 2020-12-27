from PyQt5.QtWidgets import *
from view import welcome
from model.Entry import Entry
import datetime


# starts welcome view
def run_gui():
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = welcome.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()


# entry point of program
def main():
    run_gui()


if __name__ == '__main__':
    main()
