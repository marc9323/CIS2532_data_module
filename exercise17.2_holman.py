"""
Marc D. Holman
CIS 2532 - Advanced Python Programming / Intro. Data Science
5 / 10 / 2020

Exercise 17.2
"""

import sqlite3

#  get a connection
connection = sqlite3.connect('books.db')

#  get a cursor
cursor = connection.cursor()
sql = "SELECT isbn, title, edition, copyright FROM titles"
cursor.execute(sql)

#  display fetchall and description

print("\nCURSOR.FETCHALL() \n")
print(cursor.fetchall())

print("\CURSOR.DESCRIPTION: \n")
print(cursor.description)

""" 
PROGRAM OUTPUT:

D:\COD\CIS2532_Adv_Python\Module_12_Database\venv\Scripts\python.exe D:/COD/CIS2532_Adv_Python/Module_12_Database/exercise17.2_holman.py

CURSOR.FETCHALL() 

[('0135404673', 'Intro to Python for CS and DS', 1, '2020'), ('0132151006', 'Internet & WWW How to Program', 5, '2012'), ('0134743350', 'Java How to Program', 11, '2018'), ('0133976890', 'C How to Program', 8, '2016'), ('0133406954', 'Visual Basic 2012 How to Program', 6, '2014'), ('0134601548', 'Visual C# How to Program', 6, '2017'), ('0136151574', 'Visual C++ How to Program', 2, '2008'), ('0134448235', 'C++ How to Program', 10, '2017'), ('0134444302', 'Android How to Program', 3, '2017'), ('0134289366', 'Android 6 for Programmers', 3, '2016')]
\CURSOR.DESCRIPTION: 

(('isbn', None, None, None, None, None, None), ('title', None, None, None, None, None, None), ('edition', None, None, None, None, None, None), ('copyright', None, None, None, None, None, None))

Process finished with exit code 0
"""