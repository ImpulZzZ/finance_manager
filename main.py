from PyQt5.QtWidgets import *
from view import welcome_gui as welcome_gui
from view import entry_gui as entry_gui
from view import main_gui as main_gui
from model.Entry import Entry
import datetime


# shows details of an entry
def run_show_entry_gui(entry_object):
    app = QApplication([])
    main_window = QMainWindow()
    ui = entry_gui.Ui_MainWindow()
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


# starts the main gui
def run_main_gui(entries):
    app = QApplication([])
    main_window = QMainWindow()
    ui = main_gui.Ui_MainWindow()
    ui.setupUi(main_window)

    ui.tableWidget.setColumnCount(5)

    counter = 0
    for entry in entries:

        # change table size dynamically
        ui.tableWidget.setRowCount(ui.tableWidget.rowCount() + 1)

        if entry.yearly:
            rotation = "yearly"
        if entry.monthly:
            rotation = "monthly"
        if not entry.monthly and not entry.yearly:
            rotation = "once"

        # make strings as QTableWidgetItems
        entry_name = QTableWidgetItem(entry.name)
        entry_amount = QTableWidgetItem(str(entry.amount))
        entry_pay_rotation = QTableWidgetItem(rotation)
        entry_pay_date = QTableWidgetItem(str(entry.date))
        entry_last_pay_date = QTableWidgetItem(str(entry.last_date))

        ui.tableWidget.setItem(counter, 0, entry_name)
        ui.tableWidget.setItem(counter, 1, entry_amount)
        ui.tableWidget.setItem(counter, 2, entry_pay_rotation)
        ui.tableWidget.setItem(counter, 3, entry_pay_date)
        ui.tableWidget.setItem(counter, 4, entry_last_pay_date)

        counter = counter + 1


    main_window.show()
    app.exec_()


# starts welcome view
def run_welcome_gui():
    app = QApplication([])
    main_window = QMainWindow()
    ui = welcome_gui.Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    app.exec_()


# entry point of program
def main():
    # array of all entries
    entries = []

    for x in range(0, 60):
        # insert a test entry
        test = "Test " + str(x)
        entries.append(Entry(name=test, description="Entry for test purposes", amount=512, monthly=False, yearly=True,
                             date=datetime.date(2021, 11, 27), last_date=datetime.date(2021, 12, 27)))

    run_main_gui(entries)


if __name__ == '__main__':
    main()
