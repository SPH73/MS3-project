from flask_wtf import FlaskForm, RecaptchaField
from flask_ckeditor import CKEditorField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField, IntegerField, SelectField, FieldList, FormField, DateField, Form
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
from datetime import datetime 



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
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
    submit = SubmitField('Upload') 

class CommentForm(FlaskForm):
    comment = StringField('Comment')
 
class BlogForm(FlaskForm):
    title = StringField('Title *', validators=[DataRequired()])
    content = CKEditorField('Content *', validators=[DataRequired()])
    submit = SubmitField('Send')
    
class PieceForm(FlaskForm):
    task = StringField('Task name *',validators=[DataRequired()])
    description = TextAreaField('Describe the task and expectations *', validators=[DataRequired()])
    status = SelectField('Status *', choices=['pending acceptance', 'accepted','submitted', 'closed'], validators=[DataRequired()])
    username = StringField('Username for whom the piece has been created *', validators=[DataRequired()])
    due_date = StringField('Due date *', validators=[DataRequired()])
    comment = StringField('Add a comment for your reference (recommended)')
    file_uploads = FileField('Upload a file (.pdf, .txt ,  .rtf )',validators=[FileAllowed(['pdf', 'txt', 'rtf'])])
    add_piece = SubmitField('Send Piece')
  
    
class ProjectForm(FlaskForm):
    title = StringField('Title *', validators=[DataRequired()])
    status = SelectField('Status *', choices=[('open', 'closed')], validators=[DataRequired()] )
    deadline = StringField('Set deadline', validators=[DataRequired()])
    brief = CKEditorField('Project description *', validators=[DataRequired()])
    note = StringField('Add a personal note (only visible on your dashboard)', validators=[Length(max=250, message='Must be a maximum of %d characters long (approximately 40 words).' % (250))])
    submit = SubmitField('Post Project')
       
class LanguageForm(Form):
    language = StringField('Add language', validators=[DataRequired()])

class FramworkForm(Form):
    frameworks = StringField('Add framework', validators=[DataRequired()])

class LinkForm(Form):
    name = StringField('Link name', description='e.g. GitHub')
    url = StringField('Link URL',description='e.g. https://github.com/yourusername')
    
class ProfileForm(FlaskForm):
    headline = StringField('Headline *', validators=[DataRequired(), Length(min=30, max=150)])
    bio = CKEditorField('Bio: *', validators=[Length(min=30, max=1000)])
    xp = IntegerField('Years experience *', validators=[NumberRange(min=0)])
    interests = TextAreaField("What type of projects are you interested in?", validators=[DataRequired()])
    skills = SelectField('Select', choices=['Frontend', 'Backend', 'FullStack'])
    languages = FieldList(FormField(LanguageForm), min_entries=1)
    frameworks = FieldList(FormField(FramworkForm), min_entries=1)
    links = FieldList(FormField(LinkForm), min_entries=1)
    submit = SubmitField('Send')
