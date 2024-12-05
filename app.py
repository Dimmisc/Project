import openpyxl
import sqlite3 as sq

wookbook = openpyxl.load_workbook("sales.xlsx")
worksheet, dataup = wookbook.active, []
for i in range(0, worksheet.max_row):
    c = []
    for col in worksheet.iter_cols(1, worksheet.max_column):
        c.append(col[i].value)
    dataup.append(c)
for i in range(0, worksheet.max_row):
    for col in worksheet.iter_cols(1, worksheet.max_column):
        print(col[i].value, end="\t")
    print('')

connection = sq.connect("Students.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Studentsvisit (
data TEXT,
groups TEXT,
surname TEXT,
name TEXT,
patronymic TEXT,
firstentrance TEXT,
lastexit TEXT,
attend TEXT,
status TEXT
)
''')
c = [tuple(i) for i in dataup[1::]]
for i in c:
    cursor.execute('''INSERT INTO Studentsvisit (data, groups, surname, name, patronymic, firstentrance, lastexit, attend, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', i)

connection.commit()
connection.close()
