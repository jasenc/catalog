from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, validators


class categoryForm(Form):
    # Create a name form with a max length of 80 characters to match the DB.
    name = StringField('Name', [validators.InputRequired(),
                                validators.Length(max=30,
                                message="Let's keep this to 30 characters!")])
    image = StringField('Image', [validators.InputRequired(),
                                  validators.Length(max=250,
                                  message="Let's keep this to 250 \
                                               characters!")])
    description = TextAreaField('Description', [validators.InputRequired(),
                                                validators.Length(max=250,
                                                message="Let's keep this to \
                                                250 characters!")])


class categoryItem(Form):
    # Create a name form with a max length of 80 characters to match the DB.
    name = StringField('Name', [validators.InputRequired(),
                                validators.Length(max=30,
                                message="Let's keep this to 30 characters!")])
    image = StringField('Image', [validators.InputRequired(),
                                  validators.Length(max=250,
                                  message="Let's keep this to 250 \
                                               characters!")])
    description = TextAreaField('Description', [validators.InputRequired(),
                                                validators.Length(max=250,
                                                message="Let's keep this to \
                                                250 characters!")])
