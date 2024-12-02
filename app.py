from flask import Flask, render_template
app = Flask(__name__)


@app.route('/mainpage')
def mainpage():
    return render_template('hello.html', name='hgjkhgyikhujk')
@app.route('/registration')
def Regpan():
    return render_template('Regpan.html', name='hgjkhgyikhujk')
@app.route('/Grst')
def Regpan():
    return render_template('graphics2.html', name='hgjkhgyikhujk')
@app.route('/Grstcls')
def Regpan():
    return render_template('graphics3.html', name='hgjkhgyikhujk')
@app.route('/Grstwkdys')
def Regpan():
    return render_template('graphics1.html', name='hgjkhgyikhujk')


if __name__ == '__main__':
    app.run(debug=True)
