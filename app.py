from flask import Flask
from flask import render_template
import matplotlib.pyplot as p
import matplotlib.patches as Polygon


def graph():
    x = [1, 2, 3, 4, 5]
    y = [25, 32, 34, 20, 25]
    poly = Polygon(list(zip(x, y)), facecolor='none', edgecolor='blue')
app = Flask(__name__)


@app.route('/<name>')
def hello(name):
    return render_template('hello.html', name='hgjkhgyikhujk')


if __name__ == '__main__':
    app.run(debug=True)