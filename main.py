from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

# HERE IS WHERE THE HTML TEMPLATE INFORMATION GOES

@app.route("/")
def index():
    return # add code here "form" or string format time_form.format(hours='', hours_error='') if not using templates

@app.route("/verified", methods=['POST'])
def verified():
    # add code here
    user = request.form['user']
    password = request.form['pw']
    verification = request.form['pw_ver']
    email = request.form['email']
    # validate if the text entered into the form is in the correct format

def valid_username(user):
    # add code here to verify if the user name is in the correct format. 

#  add other define functions to validate the rest of the fields

    user_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    return # add return code here

@app.route("/failed")
def failed():
    # add code here
    # return figure out the template way to return error messages

app.run()