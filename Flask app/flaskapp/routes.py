from flask import render_template, url_for, flash, redirect
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User, Post
from flaskapp import app

posts = [
    {
        'author': 'Nachiket Palkandwar',
        'title': 'First ever blog post.',
        'content': 'This blog is about the Earth.',
        'date_posted': 'August 22, 1993'
    },
    {
        'author': 'Namrata Bajoriya',
        'title': "Nammo's blog post.",
        'content': 'This blog is about the Yavatmal.',
        'date_posted': 'May 07, 1993'
    }
]


@app.route("/home")
@app.route("/")  # route() is a decorator | '/' is the root of our application
def home():
    return render_template('home.html', posts=posts)


@app.route("/register", methods=['GET', 'POST'])  # route() is a decorator | '/' is the root of our application
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])  # route() is a decorator | '/' is the root of our application
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in!", category='success')
            return redirect(url_for('home'))
        else:
            flash("Log in failed. Please check username & password.", category='danger')
    return render_template('login.html', title='Log In', form=form)


@app.route("/about")  # route() is a decorator | '/' is the root of our application
def about():
    return render_template('about.html', title="About")