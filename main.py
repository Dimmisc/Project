from flask import Flask, render_template, redirect, url_for
from database import db_session 
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from moduls.Site_moduls import main, adding
from forms.using import LoginForm
from forms.site import ExselFile
from database.site_data import Users



app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(Users, user_id)


@app.route("/")
def main_page():
    return render_template("main.html")


@app.route("/add_list", methods=["GET", "POST"])
@login_required
def excel_add():
    form = ExselFile()
    return render_template("add_visiting.html", form=form)

@app.route("/login")
def authorisation():
    form = LoginForm()
    if form.validate_on_submit:
        dbSess = db_session.create_session
        dbSess.query(Users).filter_by()
        return redirect(url_for(main_page))
    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

if __name__ == "__main__":  
    db_session.global_init("database/db/blogs.db")
    app.run(debug=True)