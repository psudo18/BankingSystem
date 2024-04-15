import sys
import re
import mysql.connector
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from ui import front, login, createacc
from datetime import datetime


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = login.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)

    def login(self):
        username = self.ui.lineEdit.text()
        if self.email_valid(username):
            pass
        else:
            return self.info_messagebox("The username is invalid! Please"
                                        " use the supported "
                                        "clients :\n\t\t@gmail.com ")
        password = self.ui.lineEdit_2.text()
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root@123",
            )
            cur = conn.cursor()
            query = "SELECT * FROM quantum_bank.users where username = %s"
            values = (username,)
            try:
                cur.execute(query, values)
                result = cur.fetchone()
                if result:
                    stored_password = result[1]
                    if stored_password == password:
                        return self.info_messagebox("********Log in Successful"
                                                    "********")
                    else:
                        return self.info_messagebox("Invalid password !!!"
                                                    " Please try again!!!")
                else:
                    return self.info_messagebox("You do not have an account!"
                                                " Please create an account!")
            except mysql.connector.Error as e:
                print(e.msg)
                return self.info_messagebox("Something went wrong :)")
        except mysql.connector.Error as err:
            print(err.msg)
            return self.info_messagebox("Connection failed !! please try "
                                        "again later !!")
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def email_valid(username):
        regex = r'\b[a-z0-9._]{5,}+@gmail\.com$'
        if re.search(regex, username):
            return True
        else:
            return False

    @staticmethod
    def info_messagebox(message):
        info_msg = QMessageBox()
        info_msg.setWindowTitle("Info!!")
        info_msg.setText(message)
        info_msg.exec()


def login_clicked():
    window1 = LoginDialog()
    window1.setWindowTitle("Log in")
    window1.exec()


class CreateAccount(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = createacc.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.checkBox.clicked.connect(self.button_enable)
        self.ui.pushButton_2.clicked.connect(self.create_account)

    def button_enable(self, checked):
        self.ui.pushButton_2.setEnabled(checked)

    def create_account(self):
        username = self.ui.lineEdit.text()
        if self.email_valid(username):
            pass
        else:
            return self.info_messagebox("The username is invalid! Please"
                                        " use the supported "
                                        "clients :\n\t\t@gmail.com ")
        password = self.ui.lineEdit_2.text()
        confirm_password = self.ui.lineEdit_3.text()
        if self.password_strength(password):
            if password != confirm_password:
                return self.info_messagebox("Your password and confirm "
                                            "password do not match! ")
        else:
            return self.info_messagebox("Please use a strong password!")
        phone_number = self.ui.lineEdit_7.text()
        if self.check(phone_number, 10):
            int(phone_number)
        else:
            return self.info_messagebox("Invalid phone no.!! "
                                        "Please enter your valid phone "
                                        "number!")
        pan = self.ui.lineEdit_8.text()
        if self.pan_validation(pan):
            pass
        else:
            return self.info_messagebox("Invalid pan no.!! "
                                        "Please enter your valid pan "
                                        "number!")
        aadhar_number = self.ui.lineEdit_9.text()
        if self.check(aadhar_number, 12):
            int(aadhar_number)
        else:
            return self.info_messagebox("Invalid aadhar no.!! "
                                        "Please enter your valid aadhar "
                                        "number!")
        name = self.ui.lineEdit_4.text()
        if self.name_validation(name):
            pass
        else:
            return self.info_messagebox("Please Enter your name correctly!!")
        dob = self.ui.lineEdit_5.text()
        if self.date_validation(dob):
            pass
        else:
            return self.info_messagebox("Enter your dob correctly"
                                        " in format YYYY-MM-DD")
        gender = self.ui.lineEdit_6.text()
        if gender == 'M' or gender == 'F':
            pass
        else:
            return self.info_messagebox("Please enter M for male "
                                        "or F for female!!!!")
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root@123",
            )
            print("Database connection successful!!")
            cur = conn.cursor()
            query = ("INSERT INTO quantum_bank.users (username, password, "
                     "phone_number,pan, aadhar_number, name, dob, gender)"
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
            values = (username, password, phone_number, pan, aadhar_number,
                      name, dob, gender)
            try:
                cur.execute(query, values)
                conn.commit()
                print(cur.rowcount, "Inserted Successfully")
                return self.info_messagebox("Congratulations! Your "
                                            "account has been created"
                                            " successfully!!")
            except mysql.connector.Error as err:
                conn.rollback()
                if err.errno == 1062:
                    column_name = err.msg.split("for key '")[1].split("'")[0]
                    print(column_name)
                    if column_name == "users.PRIMARY":
                        return self.info_messagebox("You already have an "
                                                    "account! please log in.")
                    if column_name == "users.users_pk":
                        return self.info_messagebox(f"pan: {pan} is already"
                                                    f"associated with an "
                                                    f"account!")
                    if column_name == "users.users_pk_2":
                        return self.info_messagebox(f"aadhar:a {aadhar_number}"
                                                    f" is already associated "
                                                    f"with an account!")
                else:
                    print(err.msg)
                    return self.info_messagebox(err.msg)
        except mysql.connector.Error as e:
            print(e)
            return self.info_messagebox("Something went wrong :)")
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def email_valid(username):
        regex = r'\b[a-z0-9._]{5,}+@gmail\.com$'
        if re.search(regex, username):
            return True
        else:
            return False

    @staticmethod
    def password_strength(password):
        if len(password) > 7:
            return True
        else:
            return False

    @staticmethod
    def check(phone_number, num):
        if len(phone_number) == num:
            if phone_number.isdigit():
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def pan_validation(pan):
        if len(pan) == 10:
            result = re.compile(r"[A-Z]{5}\d{4}[A-Z]")
            return result.match(pan)

    @staticmethod
    def name_validation(name):
        if len(name) > 3:
            if name.replace(" ", "").isalpha():
                return True
        else:
            return False

    @staticmethod
    def date_validation(dob):
        try:
            datetime.strptime(dob, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def info_messagebox(message):
        info_msg = QMessageBox()
        info_msg.setWindowTitle("Info!!")
        info_msg.setText(message)
        info_msg.exec()


def create_clicked():
    window2 = CreateAccount()
    window2.setWindowTitle("Create account")
    window2.exec()


class FrontDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = front.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(login_clicked)
        self.ui.pushButton_2.clicked.connect(create_clicked)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = FrontDialog()
    window.setWindowTitle("Quantum bank")
    window.show()

    app.exec()
