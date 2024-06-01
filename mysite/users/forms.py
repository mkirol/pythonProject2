from django.forms import CharField, Form


class AuthForm(Form):
    name = CharField(initial="username")
    password = CharField(initial="password")