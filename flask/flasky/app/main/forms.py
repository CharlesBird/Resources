from flask.ext.wtf import FlaskForm


class NameForm(FlaskForm):
    name = StringField('What is your name', validators=[Required()])
    submit = SubmitField('Submit')