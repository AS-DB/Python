from flask import Flask,render_template

app = Flask(__name__)

#using html tag in Flask
@app.route('/a')
def index1():
    s1='''
    <h1>Hello</h1>
'''
    return s1

#using rendered_template
@app.route('/')
def index():
    return render_template('hello.html')

if __name__=='__main__':
    app.run(debug=True)