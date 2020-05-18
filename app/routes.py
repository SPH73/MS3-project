from flask import render_template, url_for, flash, redirect, request, session
from app import app, mongo, bcrypt
from bson.objectid import ObjectId
from datetime import datetime
from app.forms import RegistrationForm, LoginForm
import bcrypt


@app.route("/")
@app.route("/home")
def home():
    return render_template('pages/home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():            
            user = mongo.db.user
            registered_username = user.find_one({'username':form.username.data})                
            if registered_username is None:
                registered_email = user.find_one({'email': form.email.data})       
                if registered_email is None:
                    hashed_pw = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
                    user.insert({'username': form.username.data, 
                             'email': form.email.data, 
                             'hashed_password': hashed_pw})                
                    flash(f'Thank you for creating an account, {form.username.data}, you may now login to access your dashboard!', 'success')
                    return redirect(url_for('login'))
                flash('That eamil is already registered. Please login.', 'info')
                return redirect(url_for('login'))                
            flash('Sorry, that username is not available, please try another.', 'info')
    return render_template('pages/register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = mongo.db.user.find_one({'username':form.username.data})
            if user:
                if bcrypt.checkpw(request.form['password'].encode('utf-8'), user['hashed_password']):
                    flash(f'Welcome back, {form.username.data}!', 'success')
                    return redirect(url_for('blog'))
                flash('Please check login details.', 'danger')
        flash('Please check login details.', 'danger')
    return render_template('pages/login.html', title='Login', form=form)

@app.route("/dashboard")
def dashboard():
    return render_template('pages/dashboard.html', title='Dashboard')

@app.route("/post")
def post():
    return render_template('pages/post.html', title='Post')

@app.route("/")
@app.route("/projects")
def projects():

    projects = mongo.db.projects.find()
    return render_template('pages/projects.html', title='Projects', projects=projects)


@app.route("/profiles")
def profiles():
    profiles = mongo.db.profiles.find()
    return render_template('pages/profiles.html', title='Profiles', profiles = profiles)


@app.route("/blog")
def blog():
    articles = mongo.db.articles.find()
    return render_template('pages/blog.html', title='Blog', articles=articles)
