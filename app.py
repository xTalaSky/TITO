from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask("_name_")
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your_secret_key')

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']

        msg = Message('Nuevo mensaje de contacto',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['titodoublep057@gmail.com'])
        msg.body = f"Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}"

        # Send the message
        mail.send(msg)
        flash("Mensaje enviado correctamente.", "success")
    except Exception as e:
        print(f"Error: {e}")
        flash("Ocurrió un error al enviar el mensaje. Intenta de nuevo más tarde.", "danger")

    return redirect(url_for('contact'))

@app.route('/')
def contact():
    return render_template('como-podemos-ayudarte.html')

@app.route('/nike')
def nike():
    return render_template('nike.html')

@app.route('/adidas')
def adidas():
    return render_template('adidas.html')

@app.route('/como-podemos-ayudarte')
def ayudarte():
    return render_template('como-podemos-ayudarte.html')

@app.route('/jordan')
def jordan():
    return render_template('jordan.html')

@app.route('/mas_populares')
def populares():
    return render_template('mas_populares.html')

@app.route('/pumas')
def pumas():
    return render_template('pumas.html')

if "_name_" == "_main_":
    app.run(debug=True)