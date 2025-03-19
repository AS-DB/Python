from  flask import Flask ,redirect,url_for


app= Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello USer"

@app.route('/admin')
def admin():
    return "Hi ADMIN!"

#string url passing in function
@app.route('/<guest>')
def guest1(guest):
    return "hello {}".format(guest)

#using redirect and url_for
@app.route('/user/<name>')
def hello_user(name):
    if name=='admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest1',guest1=name))



if __name__=="__main__":
    app.run (debug=True) 