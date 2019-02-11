from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    template = jinja_env.get_template('form.html')
    return template.render()


@app.route("/", methods=['POST'])
def verified():
    user = request.form['user']
    password = request.form['pw']
    verification = request.form['pw_ver']
    email = request.form['email']

    user_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(user) < 3 or len(user) > 20:
        password = ''
        verification = ''
        user_error = 'Usernames must be between 3 and 20 characters.'

    for char in user:
        if char == ' ':
            password = ''
            verification = ''
            user_error = 'Usernames cannot include spaces.'
    
    if len(password) < 3 or len(password) > 20:
        password_error = 'Passwords must be between 3 and 20 characters.'
        password = ''
        verification = ''
    
    for char in password:
        if char == ' ':
            password_error = 'The password field cannot include spaces.'
            password = ''
            verification = ''

    if password != verification:
        verify_error = 'Passwords do not match. Please try again.'
        password = ''
        verification = ''

    if email == '':
        email_error = ''
    else:
        if len(email) < 3 or len(email) > 20:
            password = ''
            verification = ''
            email_error = 'Email addresses must be between 3 and 20 characters.'

    at = 0
    dot = 0
    for char in email:
        if char == ' ':
            email_error = 'Email addresses cannot include spaces.'
        if char == '@':
            at += 1
        if char == '.':
            dot += 1
        if at > 1 or dot > 1:
            password = ''
            verification = ''
            email_error = "Invalid email format."
        
    if not user_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?user={0}'.format(user))
    else:
        template = jinja_env.get_template('form.html')
        return template.render(user_error=user_error, password_error=password_error, verify_error=verify_error, email_error=email_error, user=user, password=password, verification=verification, email=email)


@app.route("/welcome")
def welcome():
    user = request.args.get('user')
    template = jinja_env.get_template('welcome_message.html')
    return template.render(user=user)

app.run()