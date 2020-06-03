from flask_wtf import FlaskForm, RecaptchaField
from flask_ckeditor import CKEditorField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField, IntegerField, SelectField, FieldList, FormField, DateTimeField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, ValidationError
from datetime import datetime, timedelta 



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
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    new_password = PasswordField('New password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', 
                                     validators=[DataRequired(), EqualTo('new_password')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Update Password')    
    
    
    
class BlogForm(FlaskForm):
    author = StringField('Author *', validators=[DataRequired()])
    title = StringField('Title *', validators=[DataRequired()])
    content = CKEditorField('Content *', validators=[DataRequired()])
    submit = SubmitField('Send')
    
class PieceForm(FlaskForm):
    # subform in ProjectForm
    task = StringField('Task name')
    description = StringField('Task description')
    status = SelectField('Status', choices=['open', 'assigned', 'pending', 'closed'])
    username = StringField('Username (if assigned)', default='unassigned')
    add_piece = SubmitField('Add Piece')
  
    
class ProjectForm(FlaskForm):
    posted = DateTimeField('Post date', format=('%Y-%m-%d'))
    owner = StringField('Project owner *', validators=[DataRequired()])
    status = StringField('Status *', default='Open', validators=[DataRequired()])
    deadline = DateTimeField('Set deadline *', id="dtpicker", format=('%Y-%m-%d'))
    title = StringField('Title *', validators=[DataRequired()])
    brief = CKEditorField('Project description *', validators=[DataRequired()])
    pieces = FieldList(FormField(PieceForm))
    submit = SubmitField('Post Project')
       
             
class ListForm(FlaskForm):  
    skill = StringField('Skills *', default="Frontend Development")
    language = StringField('Languages *', default="CSS3")
    framework = StringField('Frameworks *', default="Bootstrap4")
    link = StringField('Personal Links *', default="https/github.com/username") 
    
       
class ProfileForm(FlaskForm):
    posted = DateTimeField('Post date *', default=datetime.utcnow(), 
                          validators=[DataRequired()],format='%B %d, %Y')
    first = StringField('First name')
    last = StringField('Last')   
    headline = StringField('Headline *', validators=[DataRequired(), Length(min=30, max=150)])
    bio = CKEditorField('Bio *', validators=[Length(min=30, max=1000)])
    xp = IntegerField('Years experience *', validators=[NumberRange(min=0)])
    interests = CKEditorField("Interests *", validators=[DataRequired()])
    skills = FieldList(FormField(ListForm), min_entries=2)
    languages = FieldList(FormField(ListForm), min_entries=1)
    frameworks = FieldList(FormField(ListForm), min_entries=1)
    links = FieldList(FormField(ListForm), min_entries=1)
    submit = SubmitField('Send')
