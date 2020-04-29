from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CODEFLOW_SECRET_KEY'


projects = [
    {
        'owner': "Sue Holder",
        'title': "Flask Web App",
        'brief': "Web App project brief",
        'date_posted': 'April 27, 2020'
    },
    {
        'owner': "John Doe",
        'title': "Static Website",
        'brief': "Website project brief",
        'date_posted': 'April 26, 2020'
    },
    {
        'owner': "Jane Doe",
        'title': "E-commerce Website",
        'brief': "E-commerce project brief",
        'date_posted': 'April 25, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/")
@app.route("/projects")
def project():
    return render_template('projects.html', title='Projects', projects=projects)


@app.route("/profiles")
def profile():
    return render_template('profiles.html', title='Profiles')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route("/post")
def post():
    return render_template('post.html', title='post')


if __name__ == "__main__":
    app.run(debug=True)
