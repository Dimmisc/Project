from openpyxl import load_workbook
from datetime import datetime as dt

from database.site_data import Students
from database.data import Visitings


def extand_xlsx_file(db_sess, file_href) -> str:
    wookbook = load_workbook(file_href)
    worksheet, dataup = wookbook.active, []
    for row in worksheet.iter_rows(2, worksheet.max_row):
        c = []
        for i in range(0, worksheet.max_column):
            if i == 0:
                c.append((str(row[i].value).split())[0])
                print((str(row[i].value).split())[0], end=" ")
            else:
                c.append(str(row[i].value))
                print(row[i].value, end=" ")
        dataup.append(c)
        print('')
    if db_sess:
        students = db_sess.query(Students)
    else: 
        return False
    for i in dataup:
        student = students.filter_by(name=i[3], surname=i[2], patronomic=i[4]).one()
        visit = Visitings(date=i[0],
                              grade=i[1],
                              surname=i[2],
                              name=i[3],
                              patronomic=i[4],
                              firstEnter=i[5],
                              lastExit=i[6],
                              attended=True if i[7] == 'да' else False,
                              status=i[8]
                              )
        if student:
            visit.student = student
            db_sess.add(visit)
        elif i[8] == "Обучающийся":
            new_student = Students(grade=i[1],
                                   surname=i[2],
                                   name=i[3],
                                   patronomic=i[4],
                                   )
            db_sess.add(new_student)
            visit.student = new_student
            db_sess.add(visit)
    return str(dt.today()).split()[0]