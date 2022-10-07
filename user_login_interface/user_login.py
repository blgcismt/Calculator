import sys
import sqlite3
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.set_connection()
        self.init_ui()

    def set_connection(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("Create table if not exists members (username TEXT,password TEXT)")

        self.connection.commit()


    def init_ui(self):
        self.username = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.entry = QtWidgets.QPushButton("Log in")
        self.registration = QtWidgets.QPushButton("Register")
        self.textarea = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.username)
        v_box.addWidget(self.password)
        v_box.addWidget(self.textarea)
        v_box.addStretch()
        v_box.addWidget(self.entry)
        v_box.addWidget(self.registration)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()



        self.setLayout(h_box)

        self.setWindowTitle("User Login")
        self.entry.clicked.connect(self.login)
        self.registration.clicked.connect(self.register)
        self.show()


    def login(self):
        name = self.username.text()
        pword = self.password.text()

        self.cursor.execute("Select * From members where username = ? and password = ?",(name,pword))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.textarea.setText("No such member exists \nPlease try again!")
        else:
            self.textarea.setText("Welcome "+ name)

    def register(self):
        name = self.username.text()
        pword = self.password.text()

        x = input("Please enter a username: ")
        y = input ("Please enter a password: ")

        name = x
        pword = y

        self.cursor.execute("Insert into members VALUES (?,?)",(name,pword))
        self.textarea.setText("Registered!")
        self.connection.commit()


app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec())
