from datetime import datetime
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from login.py_files.face_capture import faceCapture
from customer.pyfile.Customer_Main import Customer_Main
from admin.pyfiles.Admin_MainWindow import Admin_Main
from login.py_files.train import train
from login.py_files.faces import faces
import mysql.connector
import os

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_login_page()
        self.ui = None
        # please replace os.environ[xxx] with your own user,passwd,database
        self.mycon = mysql.connector.connect(host="localhost",
                                             user=os.environ['user'],
                                             passwd=os.environ['passwd'],
                                             database=os.environ['database'])
        self.cursor = self.mycon.cursor()

    def load_login_page(self):
        uic.loadUi('login/ui_files/Login-Page.ui', self)
        self.adminLoginBtn.clicked.connect(self.admin_login_handler)
        self.customerLoginBtn.clicked.connect(self.customer_login_handler)
        self.signupBtn.clicked.connect(self.signup)

    def signup(self):
        self.signup_page = QtWidgets.QMainWindow()
        print("signup")
        uic.loadUi('login/ui_files/signup.ui', self.signup_page)
        self.signup_page.submitBtn.clicked.connect(self.submit_handler)
        self.signup_page.backLoginBtn.clicked.connect(self.signup_page.close)
        self.signup_page.show()

    def admin_login_handler(self):
        username = self.username.text()
        password = self.password.text()
        if username == '' and password == '':
            self.pop_normal_window("You haven't input username and password!", "Please try again.")
            pass
        elif password == '':
            self.pop_normal_window("You haven't input password!", "Please try again.")
            pass
        elif username == '':
            self.pop_normal_window("You haven't input username!", "Please try again.")
            pass
        else:
            res = faces(username, password, "ADMIN")
            # res = 1
            if res == 1:
                self.admin = Admin_Main()
                self.admin.setupUi(self)
                pass
            elif res == 0:
                self.pop_normal_window("Your username and password are not matched in database", "Please try again.")
            else:
                self.pop_normal_window("Your face is not recognised", "Please try again.")
            print(4)
            pass
        pass

    def customer_login_handler(self):
        username = self.username.text()
        password = self.password.text()
        if username == '' and password == '':
            self.pop_normal_window("You haven't input username and password!", "Please try again.")
        elif password == '':
            self.pop_normal_window("You haven't input password!", "Please try again.")
        elif username == '':
            self.pop_normal_window("You haven't input username!", "Please try again.")
        else:
            res = faces(username, password, "CUSTOMER")
            # res = 1
            if res == 1:
                self.Customer = Customer_Main(username)
                self.Customer.setupUi(self)
            elif res == 0:
                self.pop_normal_window("Your username and password are not matched in database", "Please try again.")
            else:
                self.pop_normal_window("Your face is not recognised", "Please try again.")
            print(4)

    def submit_handler(self):
        print("submit")
        firstName = self.signup_page.FirstInput.text()
        lastName  = self.signup_page.LastInput.text()
        userName  = self.signup_page.UserInput.text()
        password  = self.signup_page.PasswordInput.text()
        print(firstName, lastName, userName, password)

        select = "SELECT username from Customer"
        self.cursor.execute(select)
        result = self.cursor.fetchall()

        flag = False
        for res in result:
            flag = res.__contains__(userName)
            if flag:
                break

        if len(firstName) < 1 or len(lastName) < 1 or len(userName) < 1 or len(password) < 7:
            self.pop_normal_window("You have inputted invalid information", "Please user other username.")
        elif flag:
            self.pop_normal_window("Your username has been used by other user", "Please input valid "
                                                                                "information.\nPossible reason: empty "
                                                                                "input/ password doesn't have 8 "
                                                                                "character.")
        elif QMessageBox.Yes == self.pop_ask_window("Alert", "Are you sure that you want to use " +
                                             userName + " as your username?"):
                faceCapture(userName)
                train()
                insert = "INSERT INTO CUSTOMER VALUES " \
                         "(%s, %s, %s, %s, %s, %s) "
                self.cursor.execute(insert, (userName,
                                             lastName,
                                             firstName,
                                             password,
                                             datetime.now().strftime("%H:%M:%S"),
                                             datetime.utcnow()))
                self.mycon.commit()
                print("Signup successfully.")
                self.pop_normal_window("Success",
                                       "Your information has been saved to database.")

    def pop_ask_window(self, text, question):
        message = QMessageBox()
        message.setText(question)
        message.setStyleSheet("QMessageBox{"
                                  "background-color: rgba(41,49,55,0.85);"
                                  "}"
                                  "QLabel{"
                                  "color: #FFFFFF;"
                                  "}")
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message.setDefaultButton(QMessageBox.No)
        return message.exec()

    def pop_normal_window(self, text, infoText):
        message = QMessageBox()
        message.setStyleSheet("QMessageBox{"
                              "background-color:rgba(41,49,55,0.85);"
                              "}"
                              "QLabel{"
                              "color: #FFFFFF;"
                              "}")
        message.setText(text)
        message.setInformativeText(infoText)
        message.setWindowTitle("")
        message.exec_()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyle('Oxygen')
    window = Main()
    window.show()
    sys.exit(app.exec_())
