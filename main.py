import sys
import re
import mysql.connector
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from ui import (front, login, createacc, main1, deposit, checkbalance,
                withdraw, fdm, fdc, confirmfd, fdb, transactionm,
                transactionc)
from datetime import datetime, date


def fetch_balance(acc_no):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root@123",  # Put your database password
            database='quantum_bank'
        )
        cur = conn.cursor()
        query = ("select balance from quantum_bank.accounts"
                 " where account_no = %s;")
        value = (acc_no,)
        cur.execute(query, value)
        result = cur.fetchone()
        amount = float(result[0])
        return amount
    except mysql.connector.Error as err:
        print(err.msg)
        return "Something went wrong :) "


class TraConfirm(QDialog):
    def __init__(self, acc_no, name, rec_acc):
        super().__init__()
        self.ui = transactionc.Ui_Dialog()
        self.ui.setupUi(self)
        balance = fetch_balance(acc_no)
        try:
            balance = float(balance)
        except ValueError:
            self.info("Something went wrong :)")
            self.close()
        self.ui.label.setText(f"Balance : {balance} INR ")
        self.ui.label_2.setText(f"Name : {name} ")
        self.ui.pushButton_2.clicked.connect(lambda: self.confirm(acc_no,
                                                                  balance,
                                                                  rec_acc))

    def confirm(self, acc_no, balance, rec_acc):
        amount = self.ui.lineEdit.text()
        try:
            amount = float(amount)
            balance = float(balance)
            if balance < amount:
                self.ui.lineEdit.clear()
                return self.info("Insufficient Balance! to make transaction!!")
            if amount <= 0:
                self.ui.lineEdit.clear()
                return self.info("Please enter the valid amount for transaction!")
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root@123",  # Put your database password
                database='quantum_bank'
            )
            cur = conn.cursor()
            rec_bal = fetch_balance(rec_acc)
            rec_bal = float(rec_bal)
            balance = balance - amount
            rec_bal = rec_bal + amount
            try:
                query = ("UPDATE quantum_bank.accounts set balance = %s "
                         "where account_no = %s;")
                values = (balance, acc_no)
                cur.execute(query, values)
                values = (rec_bal, rec_acc)
                cur.execute(query, values)
                conn.commit()
                self.close()
                return self.info(f"The Transaction of {amount} INR has been"
                                 f" successful to {rec_acc} ")
            except mysql.connector.Error:
                conn.rollback()
                return self.info("Something went wrong! Try again later!!")
        except TypeError:
            return self.info(f"Unable to make transaction to {rec_acc}")
        except ValueError:
            self.ui.lineEdit.clear()
            return self.info("Something went wrong!!")
        except mysql.connector.Error:
            return self.info("Something went wrong :) ")

    @staticmethod
    def info(message):
        info_msg = QMessageBox()
        info_msg.setWindowTitle("Info!!")
        info_msg.setText(message)
        info_msg.exec()


def confirm_tra(self, acc_no, name, rec_acc):
    self.close()
    window12 = TraConfirm(acc_no, name, rec_acc)
    window12.setWindowTitle("Confirm!!")
    window12.exec()


class Transaction(QDialog):
    def __init__(self, acc_no):
        super().__init__()
        self.ui = transactionm.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText(f"Account No. {acc_no} ")
        self.ui.pushButton_2.clicked.connect(lambda: self.proceed(acc_no))

    def proceed(self, acc_no):
        rec_acc = self.ui.lineEdit.text()
        if len(rec_acc) != 16:
            self.ui.lineEdit.clear()
            return self.info("Invalid Account No.!! Please enter the valid"
                             " Account No. for transaction!")
        acc_no = int(acc_no)
        try:
            receiver = int(rec_acc)
            if acc_no == receiver:
                self.ui.lineEdit.clear()
                return self.info("You cant make transaction to yourself!!!")
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root@123",  # Put your database password
                database='quantum_bank'
            )
            cur = conn.cursor()
            query = ("select name from quantum_bank.accounts where account_no"
                     "=%s;")
            value = (receiver,)
            cur.execute(query, value)
            result = cur.fetchone()
            name = result[0]
            return confirm_tra(self, acc_no, name, receiver)
        except ValueError:
            self.ui.lineEdit.clear()
            return self.info("Invalid Account No.!! ")
        except TypeError:
            self.ui.lineEdit.clear()
            return self.info("Account does not exist!! Please recheck account no.")

    @staticmethod
    def info(message):
        info_msg = QMessageBox()
        info_msg.setWindowTitle("Info!!")
        info_msg.setText(message)
        info_msg.exec()


def tra_fnc(acc_no):
    window11 = Transaction(acc_no)
    window11.setWindowTitle("Transaction")
    window11.exec()


class FDBreak(QDialog):
    def __init__(self, acc_no):
        super().__init__()
        self.ui = fdb.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText(f"Account No. {acc_no} ")
        self.info("WARNING!!! If you break your fd then you get no interest!")
        self.ui.pushButton_2.clicked.connect(lambda: self.bre_fd(acc_no))

    def bre_fd(self, acc_no):
        fd_no = self.ui.lineEdit.text()
        try:
            fd_no = int(fd_no)
            balance = fetch_balance(acc_no)
            balance = float(balance)
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root@123",  # Put your database password
                database='quantum_bank'
            )
            cur = conn.cursor()
            query = ("select amount from quantum_bank.fix_deposit where "
                     "fd_no = %s and acc_no = %s;")
            values = (fd_no, acc_no)
            cur.execute(query, values)
            try:
                result = cur.fetchone()
                amount = result[0]
                amount = float(amount)
                balance = amount + balance
                query = ("UPDATE quantum_bank.accounts set balance = %s "
                         "where account_no = %s;")
                values = (balance, acc_no)
                cur.execute(query, values)
                query = ("delete from quantum_bank.fix_deposit where fd_no"
                         " = %s and acc_no = %s;")
                values = (fd_no, acc_no)
                cur.execute(query, values)
                conn.commit()
                self.close()
                return self.info("Done! Please check your balance!")
            except ValueError:
                conn.rollback()
                return self.info("Something went wrong :)")
            except mysql.connector.Error as e:
                conn.rollback()
                return self.info(e.msg)
            except TypeError:
                conn.rollback()
                return self.info(f"Your FD of No. {fd_no} not exist!!")
        except ValueError:
            return self.info("Something went wrong! please check your fd no.")
        except mysql.connector.Error as e:
            return self.info(e.msg)

    @staticmethod
    def info(message):
        info_msg = QMessageBox()
        info_msg.setWindowTitle("Info!!")
        info_msg.setText(message)
        info_msg.exec()


def break_fd(self, acc_no):
    self.close()
    window10 = FDBreak(acc_no)
    window10.setWindowTitle("Break FD")
    window10.exec()


class FDConfirm(QDialog):
    def __init__(self, acc_no, amount, roi, years, mature_am, start_date,
                 maturity_date):
        super().__init__()
        self.ui = confirmfd.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText(f"Account No. {acc_no} ")
        self.ui.label_2.setText(f"Amount: {amount} ")
        self.ui.label_3.setText(f"Rate of Interest: {roi}% ")
        self.ui.label_4.setText(f"Time period: {years} years")
        self.ui.label_5.setText(f"FD Maturity Amount: {mature_am} ")
        self.ui.pushButton.clicked.connect(lambda: self.con_fd(acc_no,
                                                               amount,
                                                               mature_am,
                                                               roi,
                                                               start_date,
                                                               maturity_date,
                                                               years))

    def con_fd(self, acc_no, amount, mature_am, roi, start_date,
               maturity_date, years):
        balance = fetch_balance(acc_no)
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root@123",  # Put your database password
                database='quantum_bank'
            )
            cur = conn.cursor()
            balance = float(balance)
            balance = balance - amount
            query = ("UPDATE quantum_bank.accounts set balance = %s "
                     "where account_no = %s;")
            values = (balance, acc_no)
            try:
                cur.execute(query, values)
                query = ("INSERT INTO quantum_bank.fix_deposit (acc_no, "
                         "amount, maturity_amount, roi, start_date, "
                         "maturity_date, years)"
                         "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                values = (acc_no, amount, mature_am, roi, start_date,
                          maturity_date, years)
                cur.execute(query, values)
                no = cur.lastrowid
                conn.commit()
                self.close()
                return self.info(f"FD created successfully! FD No. {no}")
            except mysql.connector.Error as e:
                conn.rollback()
                return self.info(e.msg)
        except ValueError:
            return self.info(balance)
        except mysql.connector.Error as err:
            return self.info(err.msg)

    @staticmethod
    def info(message):
        info_msg = QMessageBox()
        info_msg.setWindowTitle("Info!!")
        info_msg.setText(message)
        info_msg.exec()


def confirm_fd(self, acc_no, amount, roi, years, mature_am, start_date,
               maturity_date):
    self.close()
    window9 = FDConfirm(acc_no, amount, roi, years, mature_am, start_date,
                        maturity_date)
    window9.setWindowTitle("Confirm FD")
    window9.exec()


class FDCreate(QDialog):
    def __init__(self, acc_no):
        super().__init__()
        self.ui = fdc.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText(f"Account No. {acc_no} ")
        balance = fetch_balance(acc_no)
        try:
            balance = float(balance)
        except ValueError:
            self.info(balance)
        self.ui.label_2.setText(f"Balance : {balance} INR ")
        self.ui.pushButton.clicked.connect(lambda: self.confirm(acc_no, balance))

    def confirm(self, acc_no, balance):
        amount = self.ui.lineEdit.text()
        years = self.ui.lineEdit_2.text()
        if self.a_valid(amount):
            amount = float(amount)
            if amount < 1000:
                return self.info("Insufficient amount for FD ")
            elif amount > 10000000:
                return self.info("You cant create fd of 1 cr. plus ")
        else:
            return self.info("Please enter valid amount!")
        try:
            balance = float(balance)
            if balance < amount:
                return self.info("Insufficient balance. Please check your "
                                 "balance!!")
        except ValueError:
            self.info(balance)
            self.close()
        if self.y_valid(years):
            years = int(years)
        else:
            return self.info("Please enter valid Tenure!")
        if amount in range(1000, 50000):
            if years in range(1, 5):
                roi = 5
            else:
                roi = 6
        elif amount in range(50001, 200000):
            if years in range(1, 5):
                roi = 6.5
            else:
                roi = 7.5
        elif amount in range(200001, 1000000):
            if years in range(1, 5):
                roi = 8
            else:
                roi = 9
        elif amount in range(1000001, 10000000):
            if years in range(1, 3):
                roi = 9.5
            elif years in range(3, 7):
                roi = 10.5
            else:
                roi = 12
        else:
            roi = 10

        n = 4  # compounding_frequency
        mature = amount * (1 + roi / (100 * n)) ** (n * years)
        maturity_amount = round(mature, 2)
        today = date.today()
        start_date = today
        year = today.year + years
        year = int(year)
        maturity_date = today.replace(year=year)
        print(maturity_date)
        confirm_fd(self, acc_no, amount, roi, years, maturity_amount,
                   start_date, maturity_date)

    @staticmethod
    def a_valid(amount):
        try:
            amount = float(amount)
            if amount in range(1, 10000001):
                return True
            else:
                return False
        except ValueError as err:
            print(err)
            return False

    @staticmethod
    def y_valid(years):
        try:
            years = int(years)
            if years in range(1, 11):
                return True
            else:
                return False
        except ValueError as err:
            print(err)
            return False

    @staticmethod
    def info(message):
        info_msg = QMessageBox()
        info_msg.setWindowTitle("Info!!")
        info_msg.setText(message)
        info_msg.exec()


def create_fd(self, acc_no):
    self.close()
    window8 = FDCreate(acc_no)
    window8.setWindowTitle("Create FD")
    window8.exec()


class FD(QDialog):
    def __init__(self, acc_no):
        super().__init__()
        self.ui = fdm.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText(f"Account No. {acc_no} ")
        self.ui.pushButton.clicked.connect(lambda: create_fd(self, acc_no))
        self.ui.pushButton_2.clicked.connect(lambda: break_fd(self, acc_no))


def fd_fnc(acc_no):
    window7 = FD(acc_no)
    window7.setWindowTitle("Fix Deposit")
    window7.exec()


class WithDraw(QDialog):
    def __init__(self, acc_no):
        super().__init__()
        self.ui = withdraw.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText(f"Account No. {acc_no} ")
        balance = fetch_balance(acc_no)
        try:
            balance = float(balance)
            self.ui.pushButton.clicked.connect(lambda: self.withdraw(acc_no))
        except ValueError:
            self.info_messagebox(balance)
        self.ui.label_3.setText(f"Balance : {balance} INR ")

    def withdraw(self, acc_no):
        amount = self.ui.lineEdit.text()
        self.ui.lineEdit.clear()
        balance = fetch_balance(acc_no)
        try:
            balance = float(balance)
            amount = float(amount)
            if balance >= amount:
                if amount <= 0:
                    return self.info_messagebox("Please enter the valid "
                                                "amount of INR to withdraw")
                else:
                    balance = balance - amount
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="root@123",  # Put your database password
                        database='quantum_bank'
                    )
                    try:
                        query = ("UPDATE quantum_bank.accounts set balance = %s "
                                 "where account_no = %s;")
                        values = (balance, acc_no)
                        cur = conn.cursor()
                        cur.execute(query, values)
                        conn.commit()
                        self.close()
                        return self.info_messagebox(f"The amount {amount} INR "
                                                    f"has been withdraw from your "
                                                    f"account successfully! ")
                    except mysql.connector.Error as err:
                        conn.rollback()
                        print(err)
                        return self.info_messagebox(err.msg)
            else:
                return self.info_messagebox("Please enter the amount of INR"
                                            " which is valid ")
        except ValueError:
            return self.info_messagebox("Invalid Amount to withdraw! ")

    @staticmethod
    def info_messagebox(message):
        info_msg = QMessageBox()
        info_msg.setWindowTitle("Info!!")
        info_msg.setText(message)
        info_msg.exec()


def withdraw_fnc(acc_no):
    window6 = WithDraw(acc_no)
    window6.setWindowTitle("Withdraw")
    window6.exec()


class CheckBalance(QDialog):
    def __init__(self, acc_no):
        super().__init__()
        self.ui = checkbalance.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText(f"Account No. {acc_no} ")
        self.ui.pushButton.clicked.connect(lambda: self.checking(acc_no))

    def checking(self, acc_no):
        balance = fetch_balance(acc_no)
        try:
            balance = float(balance)
            self.ui.label_2.setText(f"Balance : {balance} INR ")
        except ValueError:
            self.info_messagebox(balance)
            self.close()

    @staticmethod
    def info_messagebox(message):
        info_msg = QMessageBox()
        info_msg.setWindowTitle("Info!!")
        info_msg.setText(message)
        info_msg.exec()


def check_fnc(acc_no):
    window5 = CheckBalance(acc_no)
    window5.setWindowTitle("Balance")
    window5.exec()


class Deposit(QDialog):
    def __init__(self, acc_no):
        super().__init__()
        self.ui = deposit.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText(f"Account No: {acc_no}")
        self.ui.pushButton.clicked.connect(lambda: self.con_deposit(acc_no))

    def con_deposit(self, acc_no):
        amount = self.ui.lineEdit.text()
        self.ui.lineEdit.clear()
        try:
            amount = float(amount)
            if amount <= 0:
                return self.info_messagebox("Please Enter a valid amount "
                                            "to deposit in your account! ")
            try:
                balance = fetch_balance(acc_no)
                balance = float(balance)
                balance = balance + amount
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="root@123",  # Put your database password
                    database='quantum_bank'
                )
                query = ("UPDATE quantum_bank.accounts set balance = %s "
                         "where account_no = %s;")
                values = (balance, acc_no)
                cur = conn.cursor()
                try:
                    cur.execute(query, values)
                    conn.commit()
                    self.close()
                    return self.info_messagebox(f"The amount {amount} INR "
                                                f"has been deposit to your "
                                                f"account successfully! ")
                except mysql.connector.Error as err:
                    conn.rollback()
                    print(err.msg)
                    return self.info_messagebox(err.msg)

            except ValueError:
                self.close()
                return self.info_messagebox("Something went wrong :) ")
        except ValueError:
            return self.info_messagebox("Please Enter a valid amount "
                                        "in INR to deposit! ")

    @staticmethod
    def info_messagebox(message):
        info_msg = QMessageBox()
        info_msg.setWindowTitle("Info!!")
        info_msg.setText(message)
        info_msg.exec()


def deposit_fnc(acc_no):
    window4 = Deposit(acc_no)
    window4.setWindowTitle("Deposit")
    window4.exec()


class MainDialog(QDialog):
    def __init__(self, acc_no):
        super().__init__()
        self.ui = main1.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label_2.setText(f"Account No. {acc_no}")
        self.ui.pushButton.clicked.connect(lambda: deposit_fnc(acc_no))
        self.ui.pushButton_2.clicked.connect(lambda: withdraw_fnc(acc_no))
        self.ui.pushButton_3.clicked.connect(lambda: check_fnc(acc_no))
        self.ui.pushButton_4.clicked.connect(lambda: fd_fnc(acc_no))
        self.ui.pushButton_7.clicked.connect(lambda: tra_fnc(acc_no))


def main_dialog(acc_no):
    window3 = MainDialog(acc_no)
    window3.setWindowTitle("Account")
    window3.exec()


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
                password="root@123",   # Put your database password
                database='quantum_bank'
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
                        acc_no = result[8]
                        return main_dialog(acc_no)
                        # return self.info_messagebox("********Log in Successful"
                        #                             "********")
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
            if phone_number.startswith('0'):
                return self.info_messagebox("Your Phone NO. can't start "
                                            "with 0 Please recheck it!!")
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
        if self.age_validation(dob):
            pass
        else:
            return self.info_messagebox("You must be 18 year older to "
                                        "create an account without "
                                        "parent or guardian!!!")
        gender = self.ui.lineEdit_6.text()
        if gender == 'M' or gender == 'F':
            pass
        else:
            return self.info_messagebox("Please enter M for male "
                                        "or F for female!!!!")
        account_no = self.get_acc_no(aadhar_number)
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root@123",    # Put your database password
                database='quantum_bank'
            )
            print("Database connection successful!!")
            cur = conn.cursor()
            query = ("INSERT INTO quantum_bank.users (username, password, "
                     "phone_number,pan, aadhar_number, name, dob, gender"
                     ", account_no)"
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
            values = (username, password, phone_number, pan, aadhar_number,
                      name, dob, gender, account_no)
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
                                                    f" associated with an "
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
        if len(name) >= 3:
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
    def age_validation(dob):
        dob = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day)
                                       < (dob.month, dob.day))
        if age >= 18:
            return True
        else:
            return False

    @staticmethod
    def get_acc_no(aadhar_no):
        return int(f"18{aadhar_no}69")

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
