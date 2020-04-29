from flask import Flask, render_template, url_for, flash, redirect
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

articles = [
    {
        'author': "Sue Holder",
        'title': "New Post",
        'content': "New post content",
        'date_posted': 'April 27, 2020'
    },
    {
        'author': "John Doe",
        'title': "Interview Tips",
        'content': "Interview tips content",
        'date_posted': 'April 26, 2020'
    },
    {
        'author': "Jane Doe",
        'title': "Interesting Article",
        'content': "Interesting article content",
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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(
            f'Thank you for creating an account, {form.username.data}.', 'success')
        return redirect(url_for('blog'))
    else:
        return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Welcome back, {form.username.data}.', 'success')
        return redirect(url_for('blog'))
    else:
        return render_template('login.html', title='Login', form=form)


@app.route("/post")
def post():
    return render_template('post.html', title='Post')


@app.route("/blog")
def blog():
    return render_template('blog.html', title='Blog', articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
