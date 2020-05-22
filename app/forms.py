from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, TextAreaField, FileField, \
    IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, ValidationError
from datetime import date


class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                     validators=[DataRequired(), EqualTo('password')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class BlogForm(FlaskForm):
    author = StringField('Author')
    post_date = DateField('Post Date', default=date.today(), format='%d-%m-%Y')
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Send')

class ProjectForm(FlaskForm):
    owner = StringField('Project Owner', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
    post_date = DateField('Post Date', default=date.today(), validators=[DataRequired()],format='%d-%m-%Y')
    status = StringField('Status', default='Open', validators=[DataRequired()])
    deadline = DateField('Deadline', validators=[DataRequired()],format='%d-%m-%Y')
    title = StringField('Title', validators=[DataRequired()])
    brief = TextAreaField('Project Description', validators=[DataRequired()])
    submit = SubmitField('Send')
    
    def validate_deadline(self, deadline):
        if (self.post_date.data > self.deadline.data):
            raise  ValidationError("Deadline should be later than today.")
      
    
class ProfileForm(FlaskForm):
    post_date = DateField('Post Date', default=date.today(), validators=[DataRequired()],format='%d-%m-%Y')
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
    headline = StringField('Headline', validators=[DataRequired(), Length(min=20, max=200)])
    bio = TextAreaField('Bio', validators=[Length(min=20, max=200)])
    xp = IntegerField('Years Experience', validators=[NumberRange(min=0)])
    submit = SubmitField('Send')
        
        
