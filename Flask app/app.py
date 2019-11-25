from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6c681ab3e061cadc5ebbad267f4b8f37'

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


@app.route("/register")  # route() is a decorator | '/' is the root of our application
def regiser():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")  # route() is a decorator | '/' is the root of our application
def login():
    form = LoginForm()
    return render_template('login.html', title='Log In', form=form)


@app.route("/about")  # route() is a decorator | '/' is the root of our application
def about():
    return render_template('about.html', title="About")


if __name__ == '__main__':
    app.run(debug=True)
