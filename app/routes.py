from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import RegistrationForm, LoginForm


@app.route("/")
@app.route("/home")
def home():
    user = {'username': "Sue"}
    return render_template('pages/home.html', user=user)

@app.route("/")
@app.route("/projects")
def projects():
    projects = [
    {
        'owner': "Sue Holder",
        'title': "Flask Web App",
        'category': "Projects",
        'brief': "Web App project brief",
        'date_posted': 'April 27, 2020'
    },
    {
        'owner': "John Doe",
        'title': "Static Website",
        'category': "Projects",
        'brief': "Website project brief",
        'date_posted': 'April 26, 2020'
    },
    {
        'owner': "Jane Doe",
        'title': "E-commerce Website",
        'category': "Projects",
        'brief': "E-commerce project brief",
        'date_posted': 'April 25, 2020'
    }
]
    return render_template('pages/projects.html', title='Projects', projects=projects)


@app.route("/profiles")
def profiles():
    return render_template('pages/profiles.html', title='Profiles')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(
            f'Thank you for creating an account, {form.username.data}!', 'success')
        return redirect(url_for('blog'))
    return render_template('pages/register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'Sue' and form.password.data == 'password':
            flash(f'Welcome back, {form.username.data}!', 'success')
            return redirect(url_for('blog'))
        else:
            flash('Please check login details', 'danger')
    return render_template('pages/login.html', title='Login', form=form)


@app.route("/post")
def post():
    return render_template('pages/post.html', title='Post')


@app.route("/blog")
def blog():
    articles = [
    {
        'author': "Sue Holder",
        'title': "New Post",
        'category': "Blog",
        'content': "New post content",
        'date_posted': 'April 27, 2020'
    },
    {
        'author': "John Doe",
        'title': "Interview Tips",
        'category': "Blog",
        'content': "Interview tips content",
        'date_posted': 'April 26, 2020'
    },
    {
        'author': "Jane Doe",
        'title': "Interesting Article",
        'category': "Blog",
        'content': "Interesting article content",
        'date_posted': 'April 25, 2020'
    }
]
    return render_template('pages/blog.html', title='Blog', articles=articles)
