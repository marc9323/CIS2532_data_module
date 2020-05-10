"""
Marc D. Holman
CIS 2532 - Advanced Python Programming / Intro. Data Science
5 / 10 / 2020

Exercise 17.2
"""

import sqlite3
import pandas as pd

#  get a connection
connection = sqlite3.connect('books.db')

#  select all the authors last names from the authors table in descending order

pd.options.display.max_columns = 10

print(pd.read_sql('SELECT last FROM Authors ORDER BY last DESC', connection))

#  select all book titles from the titles table in ascending order
print(pd.read_sql('SELECT title FROM titles ORDER BY title DESC', connection))

#  use an inner join to select all the books for a specific author.  Include title,
#  copyright, year, and isbn.  Order alphabetically by title

sql = "SELECT title, copyright, edition, titles.isbn FROM titles, authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id"
print(pd.read_sql(sql, connection))

#  insert a new author into the authors table
sql = "INSERT INTO authors(first, last) VALUES ('Madhu', 'Singh')"
cursor = connection.cursor()
cursor.execute(sql)

#  insert a new title for an author.  Remember that the book must have an entry
#  in the author_isbn table and an entry in the titles table

""" 
PROGRAM OUTPUT:

D:\COD\CIS2532_Adv_Python\Module_12_Database\venv\Scripts\python.exe D:/COD/CIS2532_Adv_Python/Module_12_Database/exercise17.1_holman.py
     last
0    Wald
1   Quirk
2  Deitel
3  Deitel
4  Deitel
                              title
0         Visual C++ How to Program
1          Visual C# How to Program
2  Visual Basic 2012 How to Program
3               Java How to Program
4     Intro to Python for CS and DS
5     Internet & WWW How to Program
6                C++ How to Program
7                  C How to Program
8            Android How to Program
9         Android 6 for Programmers
                                title copyright  edition        isbn
0       Intro to Python for CS and DS      2020        1  0135404673
1       Internet & WWW How to Program      2012        5  0132151006
2                 Java How to Program      2018       11  0134743350
3                    C How to Program      2016        8  0133976890
4    Visual Basic 2012 How to Program      2014        6  0133406954
..                                ...       ...      ...         ...
235          Visual C# How to Program      2017        6  0134601548
236         Visual C++ How to Program      2008        2  0136151574
237                C++ How to Program      2017       10  0134448235
238            Android How to Program      2017        3  0134444302
239         Android 6 for Programmers      2016        3  0134289366

[240 rows x 4 columns]
"""

