from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

# HERE IS WHERE THE HTML TEMPLATE INFORMATION GOES

@app.route("/")
def index():
    return # add code here "form" if not using templates

@app.route("/verified", methods=['POST'])
def verified():
    # add code here
    # username = request.form['username']
    # password = request.form['pw']
    # verification = request.form['pw_ver']
    # email = request.form['email']
    return # add return code here

@app.route("/failed")
def failed():
    # add code here

app.run()