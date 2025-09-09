from flask import Flask, render_template, request, redirect, url_for, session
from data import USERS

app = Flask(__name__)
app.secret_key = 'dev-secret-change-me'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form.get('role')
        username = request.form.get('username', '').strip().lower()
        password = request.form.get('password', '')

        if role != 'student':
            return render_template('floginpage.html', error='Only student login is available now.')

        user = USERS.get(username)
        if not user or user['password'] != password:
            return render_template('floginpage.html', error='Invalid username or password.')

        session['student_username'] = username
        return redirect(url_for('dashboard'))

    return render_template('floginpage.html') 

@app.route('/dashboard')
def dashboard():
    username = session.get('student_username')
    if not username or username not in USERS:
        return redirect(url_for('login'))

    data = USERS[username]['data']
    return render_template('student_dashboard.html', **data)

@app.route('/logout')
def logout():
    session.pop('student_username', None)
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(debug=True)
