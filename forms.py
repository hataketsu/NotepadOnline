from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, validators


class EditForm(FlaskForm):
    content = TextAreaField('Content',validators=[validators.DataRequired()])
    save = SubmitField('Save')
