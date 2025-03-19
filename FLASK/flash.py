from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
app.secret_key='random string'

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error=None


if __name__=='__main__':
    app.run()