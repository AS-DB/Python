from flask import Flask, render_template, request, flash, redirect, url_for
from wtf import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def home():
    return redirect(url_for('contact'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash("All fields are required")
            return render_template('contact.html', form=form)
        else:
            return render_template('success.html')
    else:
        return render_template('contact.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
