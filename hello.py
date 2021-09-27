from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp

import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

expr = re.compile('.*utoronto.*')




class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()]) 
    submit = SubmitField('Submit')



class EmailForm(FlaskForm):
    email_address = StringField('What is your UofT Email Address?', validators=[DataRequired(), Email("Please include a '@' in the email address. 'email_address' is missing an '@'")])
    submit = SubmitField('Submit')





@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()

    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    email_form = EmailForm()
    form.submit = email_form.submit
    if email_form.validate_on_submit():
        old_email = session.get('email')
        if old_email is not None and old_email != email_form.email_address.data:
            flash('Looks like you have changed your email address!')
        session['email'] = email_form.email_address.data
        return redirect(url_for('index'))

    return render_template('index.html', form=form, email_form=email_form, name=session.get('name'), email_address=session.get('email'), expr=expr)

if(__name__) == '__main__':
	app.run(debug=True)

