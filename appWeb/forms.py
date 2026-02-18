from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,EmailField,SubmitField
from wtforms.validators import DataRequired,Email,NumberRange

class TribuForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired(message="Introduzca su nombre")])
    email = EmailField("Email", validators=[DataRequired(message="*Campo obligatorio"),Email(message="Introduzca un email valido")])
    edad = IntegerField("Edad", validators=[DataRequired(message="Introduzca su edad"),NumberRange (min=1,max=99, message="Introduzca edad valida")])
    submit = SubmitField("Únete")
