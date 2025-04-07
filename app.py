from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask("_name_")

app.secret_key = os.getenv('FLASK_SECRET_KEY', '123')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']

        # Crear el mensaje de correo
        msg = Message('Nuevo mensaje de contacto',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['titodoublep057@gmail.com'])  # Cambiar destinatario aquí
        msg.body = f"Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}"

        # Enviar el mensaje
        mail.send(msg)
        flash("Mensaje enviado correctamente.", "success")
    except Exception as e:
        print(f"Error: {e}")
        flash("Ocurrió un error al enviar el mensaje. Intenta de nuevo más tarde.", "danger")

    return render_template('index.html')

if "_name_" == "_main_":
    app.run(debug=True)

    