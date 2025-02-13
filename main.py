import os
from flask import Flask, render_template, redirect, url_for
from database import db_session 
from werkzeug.utils import secure_filename

from moduls.Site_moduls import main, adding
from forms.using import LoginForm
from forms.site import ExselFile
from database.site_data import Students, XLSXFILES
from database import db_session


DB_HREF = "database/db/blogs.db"
UPLOAD_FOLDER = "static/loaded"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/") 
def main_page():
    return render_template("main.html")


@app.route("/locate_student", methods=["GET", "POST"])
def locate_student():
    return render_template("locate_student.html")


@app.route("/provide_students_visiting")
def prostuvis():
    return render_template("provide_students_visiting.html")


@app.route("/provide_grade_visiting")
def prostuvis():
    return render_template("provide_students_visiting.html")


@app.route("/provide_student_visiting")
def prostuvis():
    return render_template("provide_students_visiting.html")


@app.route("/add_list", methods=["GET", "POST"])
def excel_add():
    form = ExselFile()
    if form.validate_on_submit():
        file = XLSXFILES()
        db_sess = db_session.create_session
        img_file = secure_filename(form.file.data.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], img_file)
        form.file.data.save(path)
        file.file_href = path
        db_sess.add(file)
        db_sess.commit()
    return render_template("add_visiting.html", form=form)


if __name__ == "__main__":  
    db_session.global_init(DB_HREF)
    app.run(debug=True)