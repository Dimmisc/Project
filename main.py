import os
from flask import Flask, render_template, redirect, url_for
from database import db_session 
from werkzeug.utils import secure_filename

from forms.site import ExselFile
from database.site_data import Students, XLSXFILES
from database import db_session
from moduls.Site_moduls import extand_xlsx_file, GetDataStudents, GetGradesData, GetDataStudent
from moduls.graphics import StudentsPlot, GradesPlot


DB_HREF = "database/db/blogs.db"
UPLOAD_FOLDER = "static/loaded"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"]) 
def main_page():
    db_sess = db_session.create_session()
    # extand_xlsx_file(db_sess, "static/loaded/Students.xlsx")
    # print(GetDataStudents(db_sess))
    print()
    # print(GetGradesData(db_sess))
    print()
    print(GetDataStudent(db_sess, 5))
    return render_template("panel.html")


@app.route("/provide_students_visiting", methods=["GET", "POST"])
def prostusvissearch():
    plot = StudentsPlot(db_session.create_session())
    return render_template("provide_students_visiting.html", plot=plot)


@app.route("/provide_grade_visitings", methods=["GET", "POST"])
def progravis():
    plot = GradesPlot(db_session.create_session())
    return render_template("provide_grade_visiting.html", plot=plot)


@app.route("/grade_description/<int:id_grade>")
def grades(id_grade):
    return render_template("grade_description.html")


@app.route("/provide_student_visiting/<int:id_student>", methods=["GET", "POST"])
def prostuvis(id_student):
    return render_template("provide_student_visiting.html")


@app.route("/add_list", methods=["GET", "POST"])
def excel_add():
    form = ExselFile()
    if form.validate_on_submit():
        file = XLSXFILES()
        db_sess = db_session.create_session
        img_file = secure_filename(form.file.data.filename)
        path = os.path.join(app.config['UPLOAD_FOL  DER'], img_file)
        extand_xlsx_file(db_sess, path)
        form.file.data.save(path)
        file.file_href = path
        db_sess.add(file)
        db_sess.commit()
        return redirect('/')
    return render_template("add_visiting.html", form=form, title="Добавление новой таблицы")


if __name__ == "__main__":  
    db_session.global_init(DB_HREF)
    app.run(debug=True)