
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def welcome():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    role = request.form['role']
    session['name'] = name
    session['role'] = role
    if role == 'investor':
        return redirect(url_for('index'))
    else:
        return redirect(url_for('owner'))

@app.route('/owner')
def owner():
    return render_template('owner.html')

@app.route('/index')
def index():
    name = session.get('name', '')
    return render_template('index.html', name=name)

@app.route('/opportunities')
def opportunities():
    return render_template('opportunities.html')

@app.route('/licenses')
def licenses():
    return render_template('licenses.html')

@app.route('/feasibility')
def feasibility():
    return render_template('feasibility.html')

@app.route('/support')
def support():
    return render_template('support.html')

if __name__ == '__main__':
    app.run(debug=True, port=4569)
