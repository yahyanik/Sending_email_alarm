from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True

app.config['MAIL_USERNAME'] = 'alarm.edge.system.mail@gmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False

mail = Mail(app)



@app.route('/')
def index():
    msg = Message('hello', sender= 'alarm.edge.system.mail@gmail.com', recipients= ['snikoue1@binghamton.edu','redyooy@gmail.com'], body= 'take a look at the camera stream, movement detected')
    mail.send(msg)
    return 'Message Sent!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, threaded=True, debug = True)