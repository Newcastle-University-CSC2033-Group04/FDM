from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def base():
    return redirect('home')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/games')
def games():
    return render_template('games.html')


if __name__ == '__main__':
    app.run(debug=True)
