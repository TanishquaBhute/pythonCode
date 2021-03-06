# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'library_management2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import random
import string

from login import Login
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
import library
from constants import BOOK_TYPE_AVAILABLE


class Ui_MainWindow(object):
    def __init__(self):
        self.book_details = library.prepare_library()
        self.user_name = ""
        self.assigned_books = []
        self.centralwidget = None
        self.frame = None
        self.label = None
        self.groupBox = None
        self.line_edit_username = None
        self.line_edit_password = None
        self.label_username = None
        self.label_password = None
        self.button_login = None
        self.groupBox_2 = None
        self.button_issuebook = None
        self.button_submitbook = None
        self.combo_box_booklist = None
        self.groupBox_3 = None
        self.line_edit_bookname = None
        self.line_edit_author = None
        self.line_edit_bookcode = None
        self.line_edit_category = None
        self.label_bookname = None
        self.label_author = None
        self.label_bookcode = None
        self.label_category = None
        self.groupBox_4 = None
        self.label_studentname = None
        self.label_class = None
        self.label_issued = None
        self.label_studentname_value = None
        self.label_class_value = None
        self.label_issued_value = None
        self.groupBox_5 = None
        self.tableWidget = None
        self.menubar = None
        self.statusbar = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 791, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 20, 751, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(36)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 150, 301, 251))
        self.groupBox.setObjectName("groupBox")
        self.line_edit_username = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_username.setGeometry(QtCore.QRect(110, 50, 181, 21))
        self.line_edit_username.setObjectName("line_edit_username")
        self.line_edit_password = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_password.setGeometry(QtCore.QRect(110, 100, 181, 21))
        self.line_edit_password.setObjectName("line_edit_password")
        self.label_username = QtWidgets.QLabel(self.groupBox)
        self.label_username.setGeometry(QtCore.QRect(20, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(self.groupBox)
        self.label_password.setGeometry(QtCore.QRect(20, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.button_login = QtWidgets.QPushButton(self.groupBox)
        self.button_login.setGeometry(QtCore.QRect(110, 170, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.button_login.setFont(font)
        self.button_login.setStyleSheet("background-color: rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.button_login.setObjectName("button_login")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(330, 150, 491, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.button_issuebook = QtWidgets.QPushButton(self.groupBox_2)
        self.button_issuebook.setGeometry(QtCore.QRect(310, 20, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.button_issuebook.setFont(font)
        self.button_issuebook.setObjectName("button_issuebook")
        self.button_submitbook = QtWidgets.QPushButton(self.groupBox_2)
        self.button_submitbook.setGeometry(QtCore.QRect(390, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.button_submitbook.setFont(font)
        self.button_submitbook.setObjectName("button_submitbook")
        self.combo_box_booklist = QtWidgets.QComboBox(self.groupBox_2)
        self.combo_box_booklist.setGeometry(QtCore.QRect(0, 20, 301, 22))
        self.combo_box_booklist.setObjectName("combo_box_booklist")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(330, 250, 491, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.line_edit_bookname = QtWidgets.QLineEdit(self.groupBox_3)
        self.line_edit_bookname.setGeometry(QtCore.QRect(80, 30, 181, 22))
        self.line_edit_bookname.setObjectName("line_edit_bookname")
        self.line_edit_author = QtWidgets.QLineEdit(self.groupBox_3)
        self.line_edit_author.setGeometry(QtCore.QRect(80, 90, 161, 22))
        self.line_edit_author.setObjectName("line_edit_author")
        self.line_edit_bookcode = QtWidgets.QLineEdit(self.groupBox_3)
        self.line_edit_bookcode.setGeometry(QtCore.QRect(360, 30, 111, 22))
        self.line_edit_bookcode.setObjectName("line_edit_bookcode")
        self.line_edit_category = QtWidgets.QLineEdit(self.groupBox_3)
        self.line_edit_category.setGeometry(QtCore.QRect(360, 90, 111, 22))
        self.line_edit_category.setObjectName("line_edit_category")
        self.label_bookname = QtWidgets.QLabel(self.groupBox_3)
        self.label_bookname.setGeometry(QtCore.QRect(10, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_bookname.setFont(font)
        self.label_bookname.setObjectName("label_bookname")
        self.label_author = QtWidgets.QLabel(self.groupBox_3)
        self.label_author.setGeometry(QtCore.QRect(10, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_author.setFont(font)
        self.label_author.setObjectName("label_author")
        self.label_bookcode = QtWidgets.QLabel(self.groupBox_3)
        self.label_bookcode.setGeometry(QtCore.QRect(280, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_bookcode.setFont(font)
        self.label_bookcode.setObjectName("label_bookcode")
        self.label_category = QtWidgets.QLabel(self.groupBox_3)
        self.label_category.setGeometry(QtCore.QRect(280, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_category.setFont(font)
        self.label_category.setObjectName("label_category")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 430, 291, 141))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_studentname = QtWidgets.QLabel(self.groupBox_4)
        self.label_studentname.setGeometry(QtCore.QRect(30, 30, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_studentname.setFont(font)
        self.label_studentname.setObjectName("label_studentname")
        self.label_class = QtWidgets.QLabel(self.groupBox_4)
        self.label_class.setGeometry(QtCore.QRect(30, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_class.setFont(font)
        self.label_class.setObjectName("label_class")
        self.label_issued = QtWidgets.QLabel(self.groupBox_4)
        self.label_issued.setGeometry(QtCore.QRect(30, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_issued.setFont(font)
        self.label_issued.setObjectName("label_issued")
        self.label_studentname_value = QtWidgets.QLabel(self.groupBox_4)
        self.label_studentname_value.setGeometry(QtCore.QRect(110, 30, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_studentname_value.setFont(font)
        self.label_studentname_value.setObjectName("label_studentname_value")
        self.label_class_value = QtWidgets.QLabel(self.groupBox_4)
        self.label_class_value.setGeometry(QtCore.QRect(120, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_class_value.setFont(font)
        self.label_class_value.setObjectName("label_class_value")
        self.label_issued_value = QtWidgets.QLabel(self.groupBox_4)
        self.label_issued_value.setGeometry(QtCore.QRect(110, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_issued_value.setFont(font)
        self.label_issued_value.setObjectName("label_issued_value")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(329, 430, 491, 141))
        self.groupBox_5.setObjectName("groupBox_5")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_5)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 471, 101))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 22))
        self.menubar.setObjectName("menubar")

        self.button_login.clicked.connect(self.login)
        self.combo_box_booklist.activated.connect(self.book_selected)
        self.button_issuebook.clicked.connect(self.issue_book)
        self.button_submitbook.clicked.connect(self.submit_book)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Library Management System"))
        self.groupBox.setTitle(_translate("MainWindow", "LOGIN"))
        self.label_username.setText(_translate("MainWindow", "User Name "))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.button_login.setText(_translate("MainWindow", "Login"))
        self.groupBox_2.setTitle(_translate("MainWindow", "LIBRARY"))
        self.button_issuebook.setText(_translate("MainWindow", "Issue Book"))
        self.button_submitbook.setText(_translate("MainWindow", "Submit Book"))
        self.groupBox_3.setTitle(_translate("MainWindow", "BOOK DETAILS"))
        self.label_bookname.setText(_translate("MainWindow", "Book Name"))
        self.label_author.setText(_translate("MainWindow", "Author"))
        self.label_bookcode.setText(_translate("MainWindow", "Book Code"))
        self.label_category.setText(_translate("MainWindow", "Category"))
        self.groupBox_4.setTitle(_translate("MainWindow", "STUDENT DETAILS"))
        self.label_studentname.setText(_translate("MainWindow", "Name:"))
        self.label_class.setText(_translate("MainWindow", "Class:"))
        self.label_issued.setText(_translate("MainWindow", "Issued:"))
        self.label_studentname_value.setText(_translate("MainWindow", ""))
        self.label_class_value.setText(_translate("MainWindow", ""))
        self.label_issued_value.setText(_translate("MainWindow", ""))
        self.groupBox_5.setTitle(_translate("MainWindow", "BOOK RECORDS"))

    def login(self):
        user_name = self.line_edit_username.text()
        password = self.line_edit_password.text()
        self.user_name = user_name
        login_details = Login(user_name, password)
        result = login_details.verify_login()
        if result:
            # msg = QMessageBox()
            # msg.setIcon(QMessageBox.Information)
            # msg.setText("Login Successful!")
            # msg.setWindowTitle("Login")
            # msg.exec_()
            self.label_studentname_value.setText(user_name)
            self.assigned_books = library.get_assigned_books_by_user_name(user_name)

            self.label_issued_value.setText(f"{len(self.assigned_books)} Books")
            books = [book[0] for book in library.get_books(BOOK_TYPE_AVAILABLE)]
            books.extend(self.assigned_books)

            self.combo_box_booklist.addItems(books)
            book_name = str(self.combo_box_booklist.currentText())
            self.line_edit_bookname.setText(book_name)
            self.line_edit_author.setText(self.book_details[book_name]['author'])
            self.line_edit_bookcode.setText(''.join(random.sample(string.ascii_uppercase + string.digits, 5)))
            self.line_edit_category.setText(''.join(random.choice(['Comedy', 'Horror', 'Fiction', 'History', 'Biograpy'])))

            no_columns = len(self.assigned_books[0])
            no_rows = len(self.assigned_books)
            self.tableWidget.setColumnCount(no_columns)
            self.tableWidget.setRowCount(no_rows)
            try:
                for item in self.assigned_books:
                    self.tableWidget.setItem(self.assigned_books.index(item), 0, QTableWidgetItem(item))
                    self.tableWidget.setItem(self.assigned_books.index(item), 1, QTableWidgetItem(self.book_details[item]['author']))
            except Exception as e:
                print(e)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Login Not Successful!")
            msg.setWindowTitle("Login")
            msg.exec_()

    def book_selected(self):
        book_name = str(self.combo_box_booklist.currentText())
        self.line_edit_bookname.setText(book_name)
        self.line_edit_author.setText(self.book_details[book_name]['author'])
        self.line_edit_bookcode.setText(''.join(random.sample(string.ascii_uppercase + string.digits, 5)))
        self.line_edit_category.setText(''.join(random.choice(['Comedy', 'Horror', 'Fiction', 'History', 'Biograpy'])))

    def issue_book(self):
        book_name = str(self.combo_box_booklist.currentText())
        if library.assign_book(book_name, self.user_name):
            self.refresh_ui()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Book-{book_name} is Assigned!")
            msg.setWindowTitle("Issue Book")
            msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"{book_name} is already assigned!")
            msg.setWindowTitle("Issue Book")
            msg.exec_()

    def submit_book(self):
        book_name = str(self.combo_box_booklist.currentText())
        if library.submit_book(book_name, self.user_name):
            self.refresh_ui()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Book-{book_name} is Submitted!")
            msg.setWindowTitle("Submit Book")
            msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"{book_name} in not assigned to you!")
            msg.setWindowTitle("Submit Book")
            msg.exec_()

    def refresh_ui(self):
        self.assigned_books = library.get_assigned_books_by_user_name(self.user_name)
        self.label_issued_value.setText(f"{len(self.assigned_books)} Books")
        no_columns = len(self.assigned_books[0])
        no_rows = len(self.assigned_books)
        self.tableWidget.setColumnCount(no_columns)
        self.tableWidget.setRowCount(no_rows)
        try:
            for item in self.assigned_books:
                self.tableWidget.setItem(self.assigned_books.index(item), 0, QTableWidgetItem(item))
                self.tableWidget.setItem(self.assigned_books.index(item), 1, QTableWidgetItem(self.book_details[item]['author']))
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
