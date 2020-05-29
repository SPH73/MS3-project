from flask_wtf import FlaskForm, RecaptchaField
from flask_ckeditor import CKEditorField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, TextAreaField, FileField, IntegerField, SelectField, FieldList, FormField, widgets
from wtforms.widgets import html_params, HTMLString
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, ValidationError
from datetime import datetime

class DatePickerWidget(object):
    """
    Date Time picker from Eonasdan GitHub
    https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/fieldwidgets.py#L5
    """

    data_template = (
        '<div class="input-group date appbuilder_date" id="datepicker">'
        '<span class="input-group-addon"><i class="fa fa-calendar cursor-hand"></i>'
        "</span>"
        '<input class="form-control" data-format="yyyy-MM-dd" %(text)s />'
        "</div>"
    )

    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        kwargs.setdefault("name", field.name)
        if not field.data:
            field.data = ""
        template = self.data_template

        return HTMLString(
            template % {"text": html_params(type="text", value=field.data, **kwargs)}
        )

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
    
class ListForm(FlaskForm):
    piece = StringField('Piece *')
    # skill = StringField('Skills *', default="Frontend Development")
    # language = StringField('Languages *', default="CSS3")
    # framework = StringField('Frameworks *', default="Bootstrap4")
    # link = StringField('Personal Links *', default="https/github.com/username")    
    
class BlogForm(FlaskForm):
    author = StringField('Author *', validators=[DataRequired()])
    title = StringField('Title *', validators=[DataRequired()])
    content = CKEditorField('Content *', validators=[DataRequired()])
    submit = SubmitField('Send')
    

class ProjectForm(FlaskForm):
    owner = StringField('Project owner *', validators=[DataRequired()])
    posted = DateField('Post date *', default=datetime.utcnow(), 
                          validators=[DataRequired()],format='%B %d, %Y')
    status = StringField('Status *', default='Open', validators=[DataRequired()])
    deadline = DateField('Deadline *', validators=[DataRequired()], widget=DatePickerWidget())
    title = StringField('Title *', validators=[DataRequired()])
    brief = CKEditorField('Project description *', validators=[DataRequired()])
    pieces = FieldList(FormField(ListForm), min_entries=1)
    submit = SubmitField('Send')
    
    def validate_deadline(self, deadline):
        if (self.posted.data > self.deadline.data):
            raise  ValidationError("Deadline should be later than today.") 
    
class ProfileForm(FlaskForm):
    posted = DateField('Post date *', default=datetime.utcnow(), 
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
