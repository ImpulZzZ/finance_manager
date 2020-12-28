from PyQt5.QtWidgets import *
from view import welcome as welcome
from view import entry as entry
from model.Entry import Entry
import datetime


# shows details of an entry
def show_entry(entry_object):
    app = QApplication([])
    main_window = QMainWindow()
    ui = entry.Ui_MainWindow()
    ui.setupUi(main_window)

    # change title and fill in the labels in gui
    main_window.setWindowTitle(entry_object.name)
    ui.label_for_description.setText(entry_object.description)

    # check if amount is paid monthly or yearly and change label afterwards
    if entry_object.monthly:
        when = "monthly"
    else:
        when = "yearly"

    ui.label_for_when.setText("€  " + when)

    # change number on lcd display
    ui.lcdNumber.display(entry_object.amount)

    main_window.show()
    app.exec_()


# starts welcome view
def run_gui():
    app = QApplication([])
    main_window = QMainWindow()
    ui = welcome.Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    app.exec_()


# entry point of program
def main():
    show_entry(Entry(name="Name", description="Entry for test purposes", amount=512, monthly=False, yearly=True,
                     date=datetime.date(2021, 11, 27)))


if __name__ == '__main__':
    main()
