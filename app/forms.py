from flask_wtf import FlaskForm, RecaptchaField
from flask_ckeditor import CKEditorField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField, IntegerField, SelectField, SelectMultipleField, FieldList, FormField, DateField, Form, MultipleFileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, ValidationError, URL
from flask_wtf.file import FileField, FileRequired, FileAllowed
from datetime import datetime 
from app import mongo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    passphrase = StringField("Set a security passphrase", validators=[DataRequired(), Length(min=15, max=50)])
    recaptcha = RecaptchaField()
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Sign In')
    
class ForgotPasswordForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Confirm Request')
    
class ResetPasswordForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    passphrase = StringField("Security passphrase", 
                             validators=[DataRequired(), Length(min=15, max=50)])
    new_password = PasswordField('New password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('new_password')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Reset Password')
    
class PasswordForm(FlaskForm):
    password = PasswordField('Current password', validators=[DataRequired(), Length(min=6)])
    new_password = PasswordField('New password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', 
                                     validators=[DataRequired(), EqualTo('new_password')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Update Password')    

class AccountImageForm(FlaskForm):
    image = FileField('Select image', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'])])
    recaptcha = RecaptchaField()
    submit = SubmitField('Upload') 

class BlogForm(FlaskForm):
    title = StringField('Title *', validators=[DataRequired()])
    content = CKEditorField('Content *', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UploadForm(FlaskForm):
    piece_files = MultipleFileField('Select files to upload', validators=[FileAllowed(['txt']), FileRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Upload') 

class PieceForm(FlaskForm):
    task = StringField('Task name *',validators=[DataRequired()])
    description = TextAreaField('Describe the task and expectations *', validators=[DataRequired()])
    status = SelectField('Status *', choices=['pending acceptance', 'accepted','submitted', 'closed'], validators=[DataRequired()])
    username = StringField('Username for whom the piece has been created *', validators=[DataRequired()])
    due_date = StringField('Due date *', validators=[DataRequired()])
    comment = StringField('Add a comment for your reference (recommended)')
    submit = SubmitField('Submit')
  
        
class ProjectForm(FlaskForm):
    title = StringField('Title *', validators=[DataRequired()])
    status = SelectField('Status *', default='open', choices=[('open', 'closed')], validators=[DataRequired()] )
    deadline = StringField('Set deadline', validators=[DataRequired()])
    brief = CKEditorField('Project description *', validators=[DataRequired()])
    note = StringField('Add a personal note (only visible on your dashboard)', validators=[Length(max=250, message='Must be a maximum of %d characters long (approximately 40 words).' % (250))])
    submit = SubmitField('Send')


         
class ProfileForm(FlaskForm):
    headline = StringField('Headline *', validators=[DataRequired(), Length(min=30, max=150)])
    bio = CKEditorField('Bio: *', validators=[Length(min=30, max=1000)])
    xp = IntegerField('Years experience *', validators=[NumberRange(min=0)])
    interests = TextAreaField("What type of projects are you interested in?", validators=[DataRequired()])
    stack = SelectMultipleField('Stack preference', choices=[('Front-End', 'front-end'), ('Back-End', 'back-end'), ('Full-Stack', 'full-stack')], validators=[DataRequired()])
    # 
    # CREDIT: Brian Macharia for the below code to correctly render the language choices from the database collection into a Multiple Select option in the form
    # 
    language_names = [l['language_name'] for l in mongo.db.languages.find()]
    langs = [(lang, lang.capitalize()) for lang in language_names]
    languages = SelectMultipleField('Choose your languages', choices=langs, validators=[DataRequired()])
    framework_names = [fw['framework_name'] for fw in mongo.db.frameworks.find()]
    fwks = [(fw, fw.capitalize()) for fw in framework_names]
    frameworks = SelectMultipleField('Choose your frameworks', choices=fwks, validators=[DataRequired()])
    github = StringField('GitHub', default='https://github.com/<myusername>' , validators=[URL(require_tld=True)], description='Add your username or delete the link')
    linkedin = StringField('LinkedIn', default='https://linkedin.com/in/<myusername>' , validators=[URL(require_tld=True)], description='Add your username or delete the link')
    submit = SubmitField('Submit')
    
class FeedbackForm(FlaskForm):
    feedback = TextAreaField('Feedback', validators=[DataRequired(), Length(max=500)])
    upload = FileField('Upload a reference document', validators=[FileAllowed(['.pdf'])])
    recaptcha = RecaptchaField()
    submit = SubmitField('Send') 