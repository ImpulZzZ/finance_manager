from PyQt5.QtWidgets import *
from view import welcome_gui as welcome_gui
from view import entry_gui as entry_gui
from view import new_entry_gui as new_entry_gui
from view import main_gui as main_gui
from model.Entry import Entry
import datetime

ENTRY_INFORMATION_AMOUNT = 5


def delete_by_name(entries, name):
    result = entries

    for current in result:
        if current.name == name:
            result.remove(current)

    return result


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
def run_main_gui(loaded_entries):
    #############################################################################
    def delete_button_pressed():

        # check if something is selected
        if ui.tableWidget.selectedItems():
            # delete the entry from entries array
            delete_by_name(entries, ui.tableWidget.selectedItems()[0].text())

            # get number of selected row
            row = ui.tableWidget.selectedIndexes()[0].row()

            # delete the row from gui
            ui.tableWidget.removeRow(row)

    #############################################################################
    # shows details of an entry
    def run_new_entry_gui():
        # make new instance of entry gui
        popup.setupUi(popup_window)
        popup.ok_button.clicked.connect(add_entry)
        popup_window.show()

    ##############################################################################
    # adds a new entry
    def add_entry():
        name = popup.name_field.text()

        amount = int(popup.amount_field.text())

        date = popup.date.text()
        date = date.split('.')
        date = datetime.date(int(date[2]) + 2000, int(date[1]), int(date[0]))

        # only set last date if box is checked
        if popup.checkBox_last_date.isChecked():
            last_date = popup.last_date.text()
        else:
            last_date = "1.1.01"

        last_date = last_date.split('.')
        last_date = datetime.date(int(last_date[2]) + 2000, int(last_date[1]), int(last_date[0]))

        monthly = False
        yearly = False

        # set monthly or yearly on chosen value
        if popup.choose_monthly.isChecked():
            monthly = True
        if popup.choose_yearly.isChecked():
            yearly = True

        # create new entry object
        new_entry = Entry(name, amount, monthly, yearly, date, last_date)

        # add entry to entries
        entries.append(new_entry)

        position = ui.tableWidget.rowCount()

        # add the entry details into the table
        ui.tableWidget.setRowCount(position + 1)

        if new_entry.yearly:
            new_entry_rotation = "yearly"
        if new_entry.monthly:
            new_entry_rotation = "monthly"
        else:
            new_entry_rotation = "once"

        # make strings as QTableWidgetItems
        new_entry_name = QTableWidgetItem(new_entry.name)
        new_entry_amount = QTableWidgetItem(str(new_entry.amount))
        new_entry_pay_rotation = QTableWidgetItem(new_entry_rotation)
        new_entry_pay_date = QTableWidgetItem(str(new_entry.date))
        new_entry_last_pay_date = QTableWidgetItem(str(new_entry.last_date))

        # add the entry details into the table
        ui.tableWidget.setItem(position, 0, new_entry_name)
        ui.tableWidget.setItem(position, 1, new_entry_amount)
        ui.tableWidget.setItem(position, 2, new_entry_pay_rotation)
        ui.tableWidget.setItem(position, 3, new_entry_pay_date)
        ui.tableWidget.setItem(position, 4, new_entry_last_pay_date)

        popup_window.close()

    ##############################################################################

    # list of all entries, initialized with given array
    entries = loaded_entries

    # setup the gui
    app = QApplication([])
    main_window = QMainWindow()
    ui = main_gui.Ui_MainWindow()
    ui.setupUi(main_window)

    # an entry has 5 info to be shown
    ui.tableWidget.setColumnCount(ENTRY_INFORMATION_AMOUNT)
    ui.tableWidget.setHorizontalHeaderLabels(["Name", "Amount", "Rythm", "Date", "Last Date"])

    # loop over the array of entries
    counter = 0
    for entry in entries:

        # change table size dynamically
        ui.tableWidget.setRowCount(ui.tableWidget.rowCount() + 1)

        rotation = "once"

        if entry.yearly:
            rotation = "yearly"
        if entry.monthly:
            rotation = "monthly"

        # make strings as QTableWidgetItems
        entry_name = QTableWidgetItem(entry.name)
        entry_amount = QTableWidgetItem(str(entry.amount))
        entry_pay_rotation = QTableWidgetItem(rotation)
        entry_pay_date = QTableWidgetItem(str(entry.date))
        entry_last_pay_date = QTableWidgetItem(str(entry.last_date))

        # add the entry details into the table
        ui.tableWidget.setItem(counter, 0, entry_name)
        ui.tableWidget.setItem(counter, 1, entry_amount)
        ui.tableWidget.setItem(counter, 2, entry_pay_rotation)
        ui.tableWidget.setItem(counter, 3, entry_pay_date)
        ui.tableWidget.setItem(counter, 4, entry_last_pay_date)

        counter = counter + 1

    # setup the popup gui for entry creation
    popup_window = QMainWindow()
    popup = new_entry_gui.Ui_MainWindow()

    # bind functions to the buttons
    ui.delete_button.clicked.connect(delete_button_pressed)
    ui.new_element_button.clicked.connect(run_new_entry_gui)

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
        # entries.append(Entry(name=test, amount=512, monthly=False, yearly=True,
        #                     date=datetime.date(2021, 11, 27), last_date=datetime.date(2021, 12, 27)))

    run_main_gui(entries)


if __name__ == '__main__':
    main()
