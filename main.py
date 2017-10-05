from flask import Flask, request, redirect, render_template, url_for
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('form.html')

@app.route("/signup", methods = ['POST'])

def validate_signup():
    username=request.form['username']
    password=request.form['password']
    verify=request.form['verify']
    email=request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username)<3 or len(username)>20:
        username_error = "Please enter a valid username"
        username = ''

    if len(password)<3 or len(password)>20:
        password_error = "Please enter a valid password"
        password = ''

    if verify != password:
        verify_error = "Password and verify must match"
        verify = ''
    if len(email)<3 or len(email)>20:
        email_error = "Please enter a valid email"
        email = ''
   
        return render_template('form.html')
    else:
        
        return redirect(url_for('welcome'))
        
@app.route('/welcome')   
def welcome():    
    
    return '<h1> Welcome,{0}!</h1>'.format('username')
    
if __name__ == "__main__":
 
    app.run()