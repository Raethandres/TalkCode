# coding=utf-8
from wtforms import Form, StringField, validators, PasswordField, SelectField, FieldList, DateField, FormField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.widgets import TextArea
from models import Skills
import pycountry

class Country_list(list):
    """'create choice for html form"""
    def __init__(self):
        self.lista_alpha = []
        self.lista_name = []
        self.choice = None

    def create_choices(self):
        t = list(pycountry.countries)
        for country in t:
            self.lista_alpha.append(country.alpha2)
            self.lista_name.append(country.name)
        self.choice = zip(self.lista_alpha, self.lista_name)
        return self.choice

countries = Country_list()
choices_class = countries.create_choices()

class RegisterForm(Form):
    username = StringField('',   [validators.Regexp('^\w+$', message="Regex: Username must contain only letters numbers or underscore"), validators.DataRequired(message='El campo esta vacio.'), validators.length(min=5, message='Min 5 letter, Try Again')])
    password = PasswordField('', [validators.Regexp('[A-Za-z0-9@#$%^&+=]{8,}', message="Regex: At least 8 letter"), validators.DataRequired(message='El campo esta vacio.'), validators.length(min=8, message='Min 8 letter, Try Again')])
    email = EmailField('',       [validators.Regexp('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', message="Regex: Incorrect format "), validators.Email('Ingrese un email valido'), validators.DataRequired(message='El campo esta vacio.'), validators.length(min=7, message='Min:5, letter, Try Again')])
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

class LoginForm(Form):
    username = StringField('',   [validators.DataRequired(message='El campo esta vacio.'), validators.length(min=5, message='Min 5 letter, Try Again')])
    password = PasswordField('', [validators.DataRequired(message='El campo esta vacio.'), validators.length(min=8, message='Min 8 letter, Try Again')])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None


class PersonalForm(Form):
    """Crear Regex para que solo sean letras"""
    name = StringField('First Name..', [validators.Regexp('^[A-z]+$', message="Regex: Username must contain only letters"), validators.DataRequired(message='El campo esta vacio.')])
    last_name = StringField('Last Name..',  [validators.Regexp('^[A-z]+$', message="Regex: Username must contain only letters"), validators.DataRequired(message='El campo esta vacio.')])
    sex = SelectField('Select your sex', choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgendered')])
    country = SelectField('Country', choices=choices_class)
    city = StringField('City',   [validators.DataRequired(message='El campo esta vacio.')])
    dob = DateField('DOB', format='%Y-%m-%d')
    repository = StringField('Repository', [validators.DataRequired(message='El campo esta vacio.')])
    social_red = StringField('Social', [validators.DataRequired(message='El campo esta vacio.')])


class SkillForm(Form):
    skill_field = StringField('Skill...',   [validators.DataRequired(message='El campo esta vacio.')])


class CurriculumForm(Form):
    tittle = StringField('Your tittle or Job',       [validators.DataRequired(message='El campo esta vacio.')])
    university = StringField('University o College', [validators.DataRequired(message='El campo esta vacio.')])
    description = StringField('Your description',    [validators.DataRequired(message='El campo esta vacio.')])
    skillform = FieldList(FormField(SkillForm, default=lambda: Skills()))


class QuestionForm(Form):
    tittle = StringField('',      [validators.DataRequired(message='El campo esta vacio.'), validators.length(min=5, max=150, message='Min 25, Max 150')])
    description = StringField('', [validators.DataRequired(message='El campo esta vacio.'), validators.length(min=15, max=1000, message='Min 25, Max 1000')], render_kw={"placeholder": "", "rows": 3}, widget=TextArea())
    text_area = StringField('',   [validators.DataRequired(message='El campo esta vacio.'), validators.length(min=50, max=2500, message='Min 50, Max 2000')], render_kw={"placeholder": "Code . . ."}, widget=TextArea())
    tag_one = StringField('',    [validators.length(min=2, max=25, message='Max 25')], render_kw={"placeholder": "#C++"})
    tag_two = StringField('',    [validators.length(min=2, max=25, message='Max 25')], render_kw={"placeholder": "#Python"})
    tag_three = StringField('',  [validators.length(min=2, max=25, message='Max 25')], render_kw={"placeholder": "#Databases"})


class AnswerForm(Form):
    answer_long = StringField('',    [validators.DataRequired(message='El campo esta vacio.'), validators.length(min=20, message='Min 20, Max 250')])
    text_area = StringField('',      [validators.DataRequired(message='El campo esta vacio.'), validators.length(min=8, max=2000, message='Min 8, Max 2000')], render_kw={"placeholder": "Code . . ."}, widget=TextArea())