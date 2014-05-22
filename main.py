from flask import Flask, request, render_template, redirect, url_for
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from werkzeug.security import generate_password_hash as gph
import hashlib, datetime, pymysql, sqlalchemy, re
from inno_config import *
#-------------------------------------------------------------------------------
application = Flask(__name__, template_folder="templates/"+config['hotel']['template'])
conn = pymysql.connect(host=config['sql']['host'], user=config['sql']['username'],
                       passwd=config['sql']['password'], db=config['sql']['database'], charset='utf8')
cursor = conn.cursor()
#-------------------------------------------------------------------------------

def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(application)

    @login_manager.user_loader
    def load_user(user_id):
        obj = User()
        get_id = cursor.execute("SELECT id FROM users WHERE username = '%s'"
        % obj.username)
        return get_id

class User(self):
    username = self.usr

    def __init__(self, username):
        self.usr = username


#-------------------------------------------------------------------------------

class Login(Form):
    login_user = TextField('Username', [validators.Required()])
    login_pass = PasswordField('Password', [validators.Required()])

@application.route('/index', methods=('GET', 'POST'))
def index():
    l_form = Login(request.form, prefix="login-form")
    if request.method == 'POST' and l_form.validate():
        check_login = cursor.execute("SELECT * FROM users WHERE username = '%s' AND pwd = '%s'"
        % (l_form.login_user.data, hashlib.sha1(l_form.login_pass.data).hexdigest()))
        if check_login == True:
            conn.commit()
            usr_obj = User(l_form.login.user.data)
            return redirect(url_for('me'))

    return render_template('index.html', lform=l_form)
#-------------------------------------------------------------------------------
init_login()

class Register(Form):
    username = TextField('Username', [validators.Length(min=1, max = 12)])
    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm_password', message='Passwords do not match')
    ])
    confirm_password = PasswordField('Confirm Password')
    email = TextField('Email', [validators.Length(min=6, max=35)])

def check_email(email_person_submitted):
    if re.match(r"\b[\w.-]+@[\w.-]+.\w{2,4}\b", email_person_submitted):
        pass
    else:
        redirect(url_for('index'))

@application.route('/register', methods=('GET','POST'))
def register():
    r_form = Register(request.form, prefix="register-form")
    if request.method == 'POST' and r_form.validate():
        check_reg = cursor.execute("SELECT * FROM users WHERE username = '%s' OR email = '%s'"
        % (r_form.username.data, r_form.email.data))

        if check_reg == False:
            cursor.execute("INSERT into users (username, pwd, email) VALUES ('%s','%s','%s')"
            % (r_form.username.data, hashlib.sha1(r_form.password.data).hexdigest(), check_email(r_form.email.data)))
            conn.commit()
            return redirect(url_for('index'))
    return render_template('register.html', rform=r_form)

#-------------------------------------------------------------------------------

class Me(Form):
    pass

@application.route('/me', methods=['GET'])
def me():
    form = Me(request.form)
    username = cursor.execute("")
    return render_template('me.html')

if __name__ == '__main__':
    application.run(debug=True)
