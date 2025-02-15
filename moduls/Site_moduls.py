from openpyxl import load_workbook
from datetime import datetime as dt

from database.site_data import Students
from database.data import Visitings
from database import db_session

def extand_xlsx_file(db_sess, file_href) -> str:
    print(f"Site start add data from file: {file_href}")
    wookbook = load_workbook(file_href)
    worksheet, dataup = wookbook.active, []
    for row in worksheet.iter_rows(2, worksheet.max_row):
        c = []
        for i in range(0, worksheet.max_column):
            if i == 0:
                c.append((str(row[i].value).split())[0])
            else:
                c.append(str(row[i].value))
        dataup.append(c)
    if db_sess == None:
        return False
    for i in dataup:
        print(i[3], i[2], i[4], i[8])
        student = db_sess.query(Students).filter_by(name=i[3], surname=i[2], patronomic=i[4], grade=i[1]).first()
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
        elif i[8] == "обучающиеся":
            new_student = Students(grade=i[1],
                                   surname=i[2],
                                   name=i[3],
                                   patronomic=i[4],
                                   )
            db_sess.add(new_student)
            visit.student = new_student
            db_sess.add(visit)
    db_sess.commit()
    print(f"Site ended add data from file: {file_href}")
    return str(dt.today()).split()[0]


def GetDataStudents(db_sess) -> list:
    data = []
    db_sess = db_session.create_session()
    students = db_sess.query(Students).all()
    for student in students:
        for visit in student.visits:
    return data