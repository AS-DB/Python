from  flask import Flask ,redirect,url_for,request


app= Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/welcome/<guest>')
def guest1(guest):
    return "hello {}".format(guest)


@app.route('/login',methods=['POST','GET'])

def login():
    if request.method=='POST':
        user=request.form['nm']
        return redirect(url_for('guest1',guest=user))
    else:
        user=request.args.get('nm')
        return redirect(url_for('guest1',guest=user))



if __name__=="__main__":
    app.run (debug=True) 