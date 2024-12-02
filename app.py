from flask import Flask, render_template
app = Flask(__name__)

@app.route('/mainpage')
def mainpage():
    return render_template('hello.html')
@app.route('/registration')
def Regpan():
    return render_template('Regpan.html')
@app.route('/Grst')
def studgr():
    return render_template('graphics1.html')
@app.route('/Grstcls')
def studcl():
    return render_template('graphics2.html')
@app.route('/Grstwkdys')
def studgrds():
    return render_template('graphics3.html')

if __name__ == '__main__':
    app.run(debug=True)