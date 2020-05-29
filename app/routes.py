from flask import render_template, url_for, flash, redirect, request, session
from app import app, mongo
from bson.objectid import ObjectId
from datetime import datetime
from app.forms import RegistrationForm, LoginForm, BlogForm, ProjectForm, ProfileForm, ResetPasswordForm, ForgotPasswordForm, ListForm, PasswordForm
import bcrypt

@app.route("/")
@app.route("/home")
def home():
   
    return render_template('pages/home.html')

@app.route("/blog")
def blog():
    
    articles = mongo.db.articles.find()
    return render_template('pages/blog.html', title='Blog', articles=articles)


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

# USER ACCOUNT VIEWS/ACTIONS

@app.route("/register", methods=['GET', 'POST'])
def register():
    '''First check if user has an active session, if not, check if the email address exists, if not and username isn't taken then create user.
    '''
    
    if 'username' in session:    
        flash("You are already registered and logged in. Did you mean to go to your dashboard instead?", 'info')
        return redirect(url_for('dashboard'))
        
    form = RegistrationForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():            
            user = mongo.db.user
            registered_email = user.find_one({'email': form.email.data})
                                    
            if registered_email is None:
                registered_username = user.find_one({'username':form.username.data})
                
                if registered_username is None:
                    h_phrase = bcrypt.hashpw(form.passphrase.data.encode('utf-8'), bcrypt.gensalt())
                    hashed_pw = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
                    user.insert({'username': form.username.data, 
                             'email': form.email.data,
                             'passphrase': h_phrase, 
                             'hashed_password': hashed_pw})                
                    flash(f'Thank you for creating an account, {form.username.data}, you may now login to access your dashboard!',
                          'success')
                    return redirect(url_for('login'))
                
                flash('Sorry, that username is not available, please try another.', 'info')
                return render_template('pages/register.html', title='Register', form=form)            
                        
            flash('That email is already registered. Please login.', 'info')
            return redirect(url_for('login'))
        
    return render_template('pages/register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    '''First check if user has an active session, if not, check the users credentials are correct, if so log them in and add the username to the session.
    '''
    
    if 'username' in session:
        flash("You are already logged in. Did you mean to go to your dashboard instead?", 'info')
        return redirect(url_for('dashboard'))
        
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = mongo.db.user.find_one({'username':form.username.data})
            if user and bcrypt.checkpw(request.form['password'].encode('utf-8'), user['hashed_password']):
                session['username'] = form.username.data
                flash(f'Welcome back, {form.username.data}!', 'success')
                return redirect(url_for('dashboard'))
            flash('Please check login details.', 'danger')
       
    return render_template('pages/login.html', title='Login', form=form)

@app.route("/forgot_password", methods=['GET', 'POST'])
def forgot_password():
    '''First check if user has an active session, if not, check if the email address exists and then redirect to reset password.
    '''
    
    if 'username' in session:    
        flash("You are already logged in, you can reset your password here.", 'info')
        return redirect(url_for('dashboard'))
        
    form = ForgotPasswordForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():            
            user = mongo.db.user.find_one({'email':form.email.data})

            if user:
                # Consider adding a security passphrase instead/as well
                flash("Please enter your security passphrase and create a new password", 'info')
                return redirect(url_for('reset_password'))                        
                
            flash("Email address not found!", 'danger')
            return render_template('pages/forgot.html', title='Forgot Password', form=form)
                
    return render_template('pages/forgot.html', title='Forgot Password', form=form)

@app.route("/reset_password", methods=['GET', 'POST'])
def reset_password():
    '''First check if passphrase and username are correct then update password.
    '''   
          
    form = ResetPasswordForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            
            hashed_pw = bcrypt.hashpw(form.new_password.data.encode('utf-8'), bcrypt.gensalt())
            user = mongo.db.user.find_one({'username': form.username.data})
            
            if user and bcrypt.checkpw(request.form['passphrase'].encode('utf-8'), user['passphrase']):
                mongo.db.user.find_one_and_update({'username': form.username.data}, {'$set':{'hashed_password':hashed_pw}})
                
                flash(f'Password reset was successful, {form.username.data}, you can now login.',
                          'success')
                return redirect(url_for('login'))
            
    return render_template('pages/reset.html', title='Forgot Password', form=form)

@app.route("/update_password", methods=['GET', 'POST'])
def update_password():
    '''First check if current password is correct then update password.
    '''   
    
    form = PasswordForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            
            hashed_pw = bcrypt.hashpw(form.new_password.data.encode('utf-8'), bcrypt.gensalt())
            user = mongo.db.user.find_one({'username': session['username']})
            
            if bcrypt.checkpw(request.form['password'].encode('utf-8'), user['hashed_password']):
                mongo.db.user.find_one_and_update({'username': session['username']}, {'$set':{'hashed_password':hashed_pw}})
                
                flash(f'Password reset was successful, please login again.',
                          'success')
                return redirect(url_for('login'))
            
    return render_template('pages/settings.html', title='Password', form=form)

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


@app.route("/add_article", methods=['GET','POST'])
def add_article():
    if 'username' in session:    
        article_form=BlogForm()
        if request.method == 'POST':
                article = mongo.db.articles
                if article_form.validate_on_submit():   
                    article.insert({'title': article_form.title.data,
                                    'author': article_form.author.data, 
                                'content': article_form.content.data,
                                'username': session['username'],
                                'date': datetime.utcnow()})      
                    flash('Your blog post has been created!', 'success')
                    return redirect('blog')
        return render_template('pages/addblog.html', title='New Article', article_form=article_form)
    flash('You need to be logged in to post any content.', 'info')
    return redirect(url_for('login'))

# TODO
# - EDIT AND DELETE 

@app.route('/edit_article')
def edit_article():
    pass

@app.route('/delete_article')
def delete_article():
    pass

@app.route("/add_project", methods=['GET','POST'])
def add_project():
    if 'username' in session:
        project_form=ProjectForm()
        list_form=ListForm(csrf_enabled=False)
        if request.method == 'POST':
            if project_form.validate_on_submit(): 
                flash('Your project has been posted!', 'success')
            return redirect('projects')
        return render_template('pages/addproject.html', title='New Project', project_form=project_form, list_form=list_form)
    flash('You need to be logged in to post any content.', 'info')
    return redirect(url_for('login'))

@app.route('/update_project')
def update_project():
    pass

@app.route('/delete_project')
def delete_project():
    pass


@app.route('/add_profile', methods=['GET','POST'])
def add_profile():
    if 'username' in session:        
        profile_form=ProfileForm()
        list_form=ListForm(csrf_enabled=False)
        
        if request.method == 'POST':
            if profile_form.validate_on_submit():
                flash('Your profile has been created!', 'success')
                return redirect('profiles')                      
        return render_template('pages/addprofile.html', title='Post',
                               profile_form=profile_form, list_form=list_form)
    flash('You need to be logged in to post any content.', 'info')
    return redirect(url_for('login'))
    
    
@app.route('/update_profile', methods=['POST'])
def update_profile():
    mongo.db.profiles.find_one_and_update({'username': session['username']})
    return redirect(url_for('dashboard'))

@app.route('/delete_profile', methods=['POST'])
def delete_profile():
    mongo.db.profiles.find_one_and_delete({'username': session['username']})
    return redirect(url_for('dashboard'))    





