# Note This file should only run once to create the tables and
# Triggers once in mysql database quantum_bank.
# you can change the database name as per you want
# But once this file run successfully then no need to create table
# again and again by running this. If you got an error then follow
# Manual instructions to create the table and triggers in database.

import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root@123",
        # add your password of mysql root
        database="quantum_bank"
        # database quantum_bank must be created in mysql
    )
    cur = conn.cursor()
    # The users.sql is used to create users table in database
    with open("database\\users.sql") as sql_file:
        sql_script = sql_file.read()
    cur.execute(sql_script, multi=True)
    # The accounts.sql is used to create accounts table in database.
    with open("database\\accounts.sql") as sql_file:
        sql_script = sql_file.read()
    cur.execute(sql_script, multi=True)
    # The acc_trigger.sql is used to set a trigger
    with open("database\\acc_trigger.sql") as sql_file:
        sql_script = sql_file.read()
    cur.execute(sql_script, multi=True)

    conn.commit()
    print("Success !!!")

except mysql.connector.Error as err:
    print(err.msg)
