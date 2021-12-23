from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length
import re
from wtforms.validators import ValidationError

def magnet_url(form, field):
    mag_url = field.data
    x = re.search("magnet:\?xt=urn:[a-z0-9]", mag_url)
    if x:
        pass
    else:
        raise ValidationError('Invalid Magnet url.')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=8, max=60)])
    category = SelectField("Category", choices=["Video", "Games", "Application", "Other", "Porn", "Audio"], validators=[DataRequired()])
    magnet = StringField('Magnet URL', validators=[DataRequired(), magnet_url])
    submit = SubmitField("POST")

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("LOGIN")