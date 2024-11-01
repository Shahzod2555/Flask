from wtforms.fields.simple import TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class CreatePostForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    content = TextAreaField('Текст', validators=[DataRequired()])
    submit = SubmitField('Опубликовать')
