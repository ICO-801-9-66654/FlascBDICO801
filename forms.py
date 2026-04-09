from wtforms import Form, StringField, IntegerField, EmailField
from wtforms import validators

class UserForm(Form):
    id = IntegerField("ID")
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo nombre es requerido")
    ])
    apaterno = StringField('Apaterno', [
        validators.DataRequired(message="El campo apaterno es requerido")
    ])
    amaterno = StringField('Amaterno', [
        validators.DataRequired(message="El campo amaterno es requerido")
    ])
    edad = IntegerField('Edad', [
        validators.DataRequired(message="La edad es requerida")
    ])
    email = EmailField('Correo', [
        validators.DataRequired(message="El correo es requerido"),
        validators.Email(message="Ingrese un correo válido")
    ])

class MaestrosForm(Form):
    # 1. Cambiamos a IntegerField para que coincida con la BD y quitamos el límite de longitud de texto
    matricula = IntegerField('Matricula', [
        validators.DataRequired(message="La matrícula es requerida y debe ser un número")
    ])
    
    # 2. Aumentamos el max a 50 (o 250) para que te deje escribir nombres largos
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=2, max=50, message="El nombre debe tener entre 2 y 50 caracteres")
    ])
    
    apellidos = StringField('Apellidos', [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(max=50, message="Los apellidos no pueden exceder los 50 caracteres")
    ])
    
    especialidad = StringField('Especialidad', [
        validators.DataRequired(message="Ingrese una especialidad válida"),
        validators.Length(max=50, message="La especialidad no puede exceder los 50 caracteres")
    ])
    
    # 3. Lo cambiamos a EmailField (como hiciste en UserForm) para aprovechar la validación HTML5
    email = EmailField('Email', [
        validators.DataRequired(message="El correo es requerido"),
        validators.Email(message="Ingrese un correo electrónico válido"),
        validators.Length(max=50, message="El correo no puede exceder los 50 caracteres")
    ])