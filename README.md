
# Banking System

A PySide6 project to demonstrate the various functionality of the bank.

This project uses the mysql database to store the users data and perform various operations on it.


### Notes

Creating the virtual environment for the project is recommended.

You need to install mysql database on your system or configure mysql server.




### Add-ons

Then install some python packages.


## Python packages




#### Get PySide6

```
pip install PySide6
```


#### Get mysql-connector-python

```
pip install mysql-connector-python
```



### Procedure

Firstly run the init.py only once to set up the database.

Then run the main.py file.

### Warning

You only need to run init.py for creation of table and triggers in database.

If you got error message in init.py then follow the procedure manually.



1) create database quantum_bank in mysql server.

2) Then create the table users in the database quantum_bank 
using the users.sql file from the database directory.

3) Then create the table accounts in the database quantum_bank
using the accounts.sql file from the database directory.

4) Then create the trigger in database quantum_bank using the acc_trigger.sql
file from the database directory.




## Authors

- [@psudo18](https://github.com/psudo18)


## Support

For support, email pseudomail18@gmail.com or join our [Telegram group](https://t.me/+xGwIiE5xuZRkMTll).

