from flask import Flask, render_template, redirect, url_for
from database import db_session 

from moduls.Site_moduls import main, adding
from forms.using import LoginForm
from forms.site import ExselFile
from database.site_data import Students


DB_href = "database/db/blogs.db"
app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("panel.html")




@app.route("/add_list", methods=["GET", "POST"])
def excel_add():
    form = ExselFile()
    return render_template("add_visiting.html", form=form)


if __name__ == "__main__":  
    db_session.global_init(DB_href)
    app.run(debug=True)