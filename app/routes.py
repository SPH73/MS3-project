from flask import render_template, url_for, flash, redirect, request, session
from app import app, mongo
from bson.objectid import ObjectId
from datetime import datetime
from app.forms import RegistrationForm, LoginForm, BlogForm, ProjectForm, ProfileForm
import bcrypt


@app.route("/")
@app.route("/home")
def home():
    return render_template('pages/home.html')

@app.route("/blog")
def blog():
    articles = mongo.db.articles.find()
    return render_template('pages/blog.html', title='Blog', articles=articles)

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
            if user and bcrypt.checkpw(request.form['password'].encode('utf-8'), user['hashed_password']):
                session['username'] = form.username.data
                flash(f'Welcome back, {form.username.data}!', 'success')
                return redirect(url_for('dashboard'))
            flash('Please check login details.', 'danger')
        flash('Please check login details.', 'danger')
    return render_template('pages/login.html', title='Login', form=form)

@app.route('/logout')
def logout():
       # remove the username from the session if it is there
   session.pop('username', None)
   flash('You have logged out.', 'success')
   return redirect(url_for('home'))
    

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
        if 'username' in session:
            user_profile = mongo.db.profiles.find_one({'username': session['username']})
            user_projects = mongo.db.projects.find({'username': session['username']})
            profile_messages = mongo.db.profile_messages.find({'username': session['username']})
            project_messages = mongo.db.project_messages.find({'username': session['username']})            
            return render_template('pages/dashboard.html', 
                                title='Dashboard',
                                user_profile=user_profile, 
                                user_projects=user_projects, 
                                profile_messages=profile_messages,
                                project_messages=project_messages)
            
        flash('You need to be logged in to access your dashboard.', 'warning')
        return redirect(url_for('login'))

@app.route("/post", methods=['GET', 'POST'])
def post():
    if 'username' in session:        
        article_form=BlogForm()
        project_form=ProjectForm()
        profile_form=ProfileForm()
        if request.method == 'POST':
            if article_form.validate_on_submit():
                flash('Your blog post has been created!', 'success')
                return redirect('blog')
            elif project_form.validate_on_submit(): 
                flash('Your project has been created!', 'success')
                return redirect('projects')
            elif profile_form.validate_on_submit():
                flash('Your profile has been created!', 'success')
                return redirect('profiles')                      
        return render_template('pages/post.html', title='Post', 
                                article_form=article_form, project_form=project_form, profile_form=profile_form)
    flash('You need to be logged in to post any content.', 'info')
    return redirect(url_for('login'))

@app.route("/")
@app.route("/projects")
def projects():
    if 'username' in session:
        projects = mongo.db.projects.find()
        return render_template('pages/projects.html', title='Projects', projects=projects)
    flash('Please login to view user projects.', 'warning')
    return redirect(url_for('login'))


@app.route("/profiles")
def profiles():
    if 'username' in session:
        profiles = mongo.db.profiles.find()
        return render_template('pages/profiles.html', title='Profiles', profiles = profiles)
    flash('Please login to view user profiles.', 'warning')
    return redirect(url_for('login'))


