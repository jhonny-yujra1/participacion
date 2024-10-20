from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Cambia esto a una clave secreta única

# Datos de usuario simulados (en un caso real, usarías una base de datos)
usuarios = {
    'usuario1': 'contraseña1',
    'usuario2': 'contraseña2',
    'JHONNY':'123'
}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in usuarios and usuarios[username] == password:
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            flash('Nombre de usuario o contraseña incorrectos', 'error')

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    return render_template('welcome.html', username=username)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)