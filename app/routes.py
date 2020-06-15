from flask import render_template, url_for, flash, redirect, request, session
from app import app, mongo
from bson.objectid import ObjectId
import pymongo
from datetime import datetime
from app.forms import RegistrationForm, LoginForm, BlogForm, ProjectForm, ProfileForm, ResetPasswordForm, ForgotPasswordForm, PieceForm, PasswordForm, ListForm
import bcrypt



@app.route("/")
@app.route("/home")
def home():
   
    return render_template('pages/home.html')



# USER ACCOUNT VIEWS/ACTIONS

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Checks if user has an active session, if not, checks if the email address exists, if not and username isn't taken then creates user.
    """
    
    if 'username' in session:    
        flash('You are already registered and logged in. Did you mean to go to your dashboard instead?', 'info')
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    """First checks if user has an active session, if not, checks the users credentials are correct, if so logs them in and adds the username to the session.
    """
    
    if 'username' in session:
        flash('You are already logged in. Did you mean to go to your dashboard instead?', 'info')
        return redirect(url_for('dashboard'))
        
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = mongo.db.user.find_one({'username':form.username.data})
            if user and bcrypt.checkpw(request.form['password'].encode('utf-8'), user['hashed_password']):
                session['username'] = form.username.data
                current_user = session['username']
                flash(f'Welcome back, {current_user}!', 'success')
                return redirect(url_for('dashboard'))
            flash('Please check login details.', 'danger')
       
    return render_template('pages/login.html', title='Login', form=form)

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    """First checks if user has an active session, if not, checks if the email address exists and then redirects to reset password.
    """
    
    if 'username' in session:    
        flash('You are already logged in, you can reset your password here.', 'info')
        return redirect(url_for('dashboard'))
        
    form = ForgotPasswordForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():            
            user = mongo.db.user.find_one({'email':form.email.data})

            if user:
                flash('Please enter your security passphrase and create a new password', 'info')
                return redirect(url_for('reset_password'))                        
                
            flash('Email address not found!', 'danger')
            return render_template('pages/forgot.html', title='Forgot Password', form=form)
                
    return render_template('pages/forgot.html', title='Forgot Password', form=form)

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    """First checks if passphrase and username are correct then updates new password in database.
    """   
          
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

@app.route('/update_password', methods=['GET', 'POST'])
def update_password():
    """First checks if the users current password is correct then updates the password in the database.
    """   
    
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
    """Removes the username from the session.
    """
    
    session.pop('username', None)
    flash('You have logged out.', 'success')
    return redirect(url_for('home'))
    

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    """First checks the user is logged in then renders the users content to the dashboard template.
    """
    
    if 'username' in session:
        user_profile = mongo.db.profiles.find_one({'username': session['username']})
        user_projects = mongo.db.projects.find({'username': session['username']})
        profile_messages = mongo.db.profile_messages.find({'username': session['username']})
        project_messages = mongo.db.project_messages.find({'username': session['username']})            
        return render_template('pages/dashboard.html', 
                            title='Dashboard',            
                            profile=user_profile, 
                            projects=user_projects, 
                            profile_messages=profile_messages,
                            project_messages=project_messages)
        
    flash('You need to be logged in to access your dashboard.', 'warning')
    return redirect(url_for('login'))

# BLOG ARTICLE VIEWS

@app.route('/blog')
def blog():
    """Retrieves all the documents from the articles collection and dislpay them in order of newest to oldest.
    """
    
    articles = mongo.db.articles.find().sort('date',pymongo.DESCENDING)
                     
    return render_template('pages/blog.html', title='Blog', articles=articles, legend='Read the latest articles')


@app.route('/add_article', methods=['GET','POST'])
def add_article():
    """Checks if the user is logged in then renders the form to add a blog article. If the form validates, retrieves the users id and includes it with the form data to the articles collection.
    """
    
    if 'username' in session:           
        form=BlogForm()        
        if request.method == 'POST':
            if form.validate_on_submit():
                user = mongo.db.user.find_one({'username': session['username']})    
                mongo.db.articles.insert_one({'title': form.title.data,
                                'content': form.content.data,
                                'author': session['username'],
                                'date': datetime.utcnow(),
                                'user_id': user['_id']})
                 
                flash('Your blog post has been created!', 'success')
                return redirect(url_for('blog'))
            
        return render_template('pages/addarticle.html', title='New Article', article_form=form, legend="Create Your Blog Article")
    
    flash('You need to be logged in to post any content.', 'info')
    return redirect(url_for('login'))


@app.route('/edit_article/<article_id>')
def edit_article(article_id):
    """First checks that the user is logged in then renders the form with the data from the collection document. (Edit button only appears if there is a match with the user id in the database for the particular document id).
    """
    
    if 'username' in session: 
        article = mongo.db.articles.find_one_or_404(
            {'_id': ObjectId(article_id)})
        form=BlogForm()
        form.title.data = article['title']
        form.content.data = article['content']
        return render_template('pages/editarticle.html', form=form, article=article, legend='Edit your Blog Article')

@app.route('/update_article/<article_id>', methods=['POST'])
def update_article(article_id):
    """When the user submits the edited content, the document in the collection is updated with the changes and redirects the user to the blog page.
    """
    
    article = mongo.db.articles
    article.find_one_and_update({'_id': ObjectId(article_id) },
                                {'$set':
                                    {'title': request.form.get('title'),
                                     'content': request.form.get('content')}})
    flash('Your post has been updated.' 'success')
    return redirect(url_for('blog'))
    

@app.route('/delete_article/<article_id>', methods=['POST'])
def delete_article(article_id):
    '''If the user is logged in and the user id is located in the document then the document is removed from the collection. (Client-side confirmation is passed before the user reaches this view function.)
    '''
    
    article = mongo.db.articles
    article.delete_one({'_id': ObjectId(article_id)})
    flash('Your blog article has been deleted.', 'success')
    return redirect(url_for('blog'))

@app.route('/add_comment/<article_id>', methods=['GET', 'POST'])
def add_comment(article_id):
    """If a user is logged in, adds a comment in the article collection comments array and creates a reference document in the comments collection for user dashboards.
    """

    article = mongo.db.articles
    if 'username' in session:
        if request.method == 'POST':
            comment = mongo.db.article_comments
            user = mongo.db.user.find_one({'username': session['username']})
            article.find_one_and_update({'_id': ObjectId(article_id) },{
                '$push':{'comments':{'username': session['username'],
                                      'date': datetime.utcnow(),
                                      'text': request.form.get('comment')}}})
            comment.insert_one({'user': user['_id'],
                                'from_user': session['username'],
                                'article': article['_id'],
                                'article_title': article['title'],
                                'date': datetime.utcnow(),
                                'to_user': article['username'],
                                'text': request.form.get('comment')})
            flash('Your comment has been added.', 'success')
        return render_template('pages/blog.html')
    flash('Please login to post a comment.', 'info')
    return redirect(url_for('login'))



# PROJECT VIEWS

@app.route("/projects")
def projects():
    """First check that the user is logged in, then display all the projects in the database sorted by newest first.
    """
    
    if 'username' in session:
        current_user = mongo.db.user.find_one({'username': session['username']})      
        projects = mongo.db.projects.find().sort('date',pymongo.DESCENDING)
        return render_template('pages/projects.html', title='Projects', projects=projects, current_user=current_user)
    
    flash('Please login to view user projects.', 'warning')
    return redirect(url_for('login'))

                 
@app.route('/add_project', methods=['GET','POST'])
def add_project():
    """First checks that the user is logged in before rendering the form. When the form is validated, the users user_id is retireved and add with the form content with the current date and time to the collection.
    """
    
    if 'username' in session:        
        form=ProjectForm()
        
        if request.method == 'POST':
            if form.validate_on_submit():
                user = mongo.db.user.find_one({'username': session['username']})
                mongo.db.projects.insert_one({'username': session['username'],
                                    'date': datetime.utcnow(),
                                    'title': form.title.data,
                                    'deadline': datetime.strptime(form.deadline.data, "%d/%m/%Y"),
                                    'brief': form.brief.data,
                                    'status': form.status.data,
                                    'user_id': user['_id']})
                
                flash('Your project has been created.', 'success')
                return redirect(url_for('projects'))
            
        return render_template('pages/addproject.html', title='New Project',  form=form)
        
    flash('You need to be logged in to post any content.', 'info')
    return redirect(url_for('login'))        
            

@app.route('/edit_project<project_id>')
def edit_project(project_id):
    """First checks that the user is logged in then renders the form with the data from the collection document. (Edit button only appears if there is a match with the user id in the database for the particular document id and the users session data).
    """
    
    if 'username' in session: 
        project = mongo.db.projects.find_one_or_404(
            {'_id': ObjectId(project_id)})
        form=ProjectForm()
        form.title.data = project['title']
        form.status.data = project['status']
        form.deadline.data = project['deadline']
        form.brief.data = project['brief']
        return render_template('pages/editproject.html', form=form, project=project, legend='Edit your project')

@app.route('/update_project<project_id>', methods=['POST'])
def update_project(project_id):
    """When the user submits the edited content, the document in the collection is updated with the changes and redirects the user to the projects page.
    """

    project = mongo.db.projects
    project.find_one_and_update({'_id': ObjectId(project_id) },
                                {'$set':
                                    {'title': request.form.get('title'),
                                     'status': request.form.get('status'),
                                     'deadline': datetime.strptime(request.form.get('deadline'), '%m/%d/%Y'),
                                     'brief': request.form.get('brief')}})
    return redirect(url_for('projects'))

@app.route('/delete_project<project_id>', methods=['POST'])
def delete_project(project_id):
    """If the user is logged in and the user id is located in the document then the document is removed from the collection. (Client-side confirmation is passed before the user reaches this view function.)
    """
    
    project = mongo.db.projects
    project.delete_one({'_id': ObjectId(project_id)})
    flash('Your project has been deleted.', 'success')
    return redirect(url_for('projects'))

@app.route('/add_piece/<title>', methods=['GET', 'POST'])
def add_piece(title):
    """TO DO WHEN function complete!!!!
    """
    
    if 'username' in session:
        form=PieceForm()
        
        if request.method == 'POST':
            if form.validate_on_submit():
                project = mongo.db.projects.find_one_or_404({'title': title})
                piece = mongo.db.pieces.insert({'task': piece.task.data,
                                  'description': piece.description.data,
                                  'status': piece.status.data,
                                  'username': piece.username.data,
                                  'due_date': piece.due_date.data,
                                  'project_id': project._id})
                piece_id = piece.inserted_id
                project.pieces.insert_one({'pieces': [{piece_id}]})
                return redirect(url_for('dashboard'))
                
        return render_template('pages/addproject.html', title='New Project', form=form, project_id=project)
    
    flash('You need to be logged in to post any content.', 'info')
    return redirect(url_for('login'))

# PROFILE VIEWS

@app.route("/profiles")
def profiles():
    """Checks if is the user is logged in first and then renders page with profile collection data.
    """
    
    if 'username' in session:
        profiles = mongo.db.profiles.find()
        return render_template('pages/profiles.html', title='Profiles', profiles = profiles)
    flash('Please login to view user profiles.', 'warning')
    return redirect(url_for('login'))


@app.route('/add_profile', methods=['GET','POST'])
def add_profile():
    """Checks if the user has an active session and an exisiting profile for the user doesn't exist before renders the form. When the form is validated first retrieves the user_id to include it with the form data to the database collection with the current date and time.
    """
    
    if 'username' in session:
        user = mongo.db.user.find_one({'username': session['username']})           
        form=ProfileForm()
        list_form=ListForm(csrf_enabled=False)
        
        if request.method == 'POST':
            if form.validate_on_submit():                    
                mongo.db.profiles.insert_one({'headline': form.headline.data,
                                              'bio': form.bio.data,
                                              'username': session['username'],
                                              'date': datetime.utcnow(),
                                              'xp': form.xp.data,
                                              'interests': form.interests.data,
                                              'user_id': user['_id']})
                flash('Your profile has been created.', 'success')
                return redirect('profiles')
            
        elif request.method == 'GET':
            pro = mongo.db.profiles.find_one({'user_id': user['_id']})
            if pro:
                flash('Sorry, only one profile per user permitted. Would you like to edit your existing profile?', 'info')
                return redirect(url_for('dashboard'))
            
            return render_template('pages/addprofile.html', title='Post',
                               form=form, list_form=list_form, legend='Create your profile')
        
    flash('You need to be logged in to post any content.', 'info')
    return redirect(url_for('login'))
    
@app.route('/edit_profile/<profile_id>')
def edit_profile(profile_id):
    """Checks if the user is logged in and the user_id matches with the document, then renders the form with the existing values. 
    """
    
    profile = mongo.db.profiles.find_one_or_404(
        {'_id': ObjectId(profile_id)})
    form=ProfileForm()
    form.headline.data = profile['headline']
    form.bio.data = profile['bio']
    form.xp.data = profile['xp']
    form.interests.data = profile['interests']
    return render_template('pages/editprofile.html', form=form, profile=profile, legend='Edit your Profile')
    
@app.route('/update_profile/<profile_id>', methods=['POST'])
def update_profile(profile_id):
    """When the form is submitted, the collection is updated with the changes and the current date and time.
    """
    
    profile = mongo.db.profiles
    profile.find_one_and_update({'_id': ObjectId(profile_id)},
                                {'$set': {'date': datetime.utcnow(),
                                          'headline': request.form.get('headline'),
                                          'bio': request.form.get('bio'),
                                          'xp': request.form.get('xp'),
                                          'interests': request.form.get('interests')}})
    return redirect(url_for('dashboard'))


@app.route('/delete_profile/<profile_id>', methods=['POST'])
def delete_profile(profile_id):
    """If the user is logged in and their id matches the document, the document is removed from the database collection. (Client-side validation passed before the user reaches the view function.)
    """
    
    profile = mongo.db.profiles
    profile.delete_one({'_id': ObjectId(profile_id)})
    flash('Your profile has been deleted.', 'success')
    return redirect(url_for('dashboard'))







