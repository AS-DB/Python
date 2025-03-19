from  flask import Flask ,redirect,url_for


app= Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello USer"

#string
@app.route('/admin')
def admin():
    return "Hi ADMIN!"
#Int
@app.route('/<int:num>')
def square(num):
    return "square of {} is {}".format(num,num*num)

# Route to handle multiple integers
@app.route('/sum/<int:num1>/<int:num2>')
def sum_of_numbers(num1, num2):
    total = num1 + num2
    return "Sum of {} and {} is {}".format(num1, num2, total)

if __name__=="__main__":
    app.run (debug=True) 