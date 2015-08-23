from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, validators
from wtforms.fields.html5 import DateField


class categoryForm(Form):
    # Create a name form with a max length of 80 characters to match the DB.
    name = StringField('Name', [validators.InputRequired(),
                                validators.Length(max=80,
                                message="Let's keep this to 80 characters!")])
    address = StringField('Address', [validators.InputRequired(),
                                      validators.Length(max=250,
                                      message="Let's keep this to 250 \
                                               characters!")])
    city = StringField('City', [validators.InputRequired(),
                                validators.Length(max=80,
                                message="Sorry, cities are at most 80\
                                         characters!")])
    state = StringField('State', [validators.InputRequired(),
                                  validators.Length(max=2,
                                  message="Sorry, states are 2\
                                           characters!")])
    zipCode = StringField('zipCode', [validators.InputRequired(),
                                      validators.Length(max=6,
                                      message="Sorry, zipCodes are at most 10\
                                               characters!")])
    website = StringField('Website', [validators.InputRequired()])


class itemForm(Form):
    name = StringField('Name', [validators.InputRequired(),
                                validators.Length(max=80,
                                message="Let's keep this to 80 characters!")])
    gender = StringField('Gender', [validators.InputRequired(),
                                    validators.Length(max=6,
                                    message="Sorry, genders are at most 6\
                                            characters!")])
    dateOfBirth = DateField("Date of Birth", [validators.InputRequired()])
    picture = StringField('Picture', [validators.InputRequired()])
    weight = IntegerField('Weight', [validators.InputRequired(),
                                     validators.NumberRange(min=1, max=10,
                                     message="Between 1 and 10")])
