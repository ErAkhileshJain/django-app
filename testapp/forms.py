from django import forms
import re


class UserForm(forms.Form):
    username = forms.CharField(
        label='Name',
        required=False,
        min_length=3,
        max_length=20,
        help_text='Name must have min 3 char',
        error_messages={
            'required': "Name can't be blank",
            'min_length': 'Message..!'
        }

    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Email'
        })
    )
    address = forms.CharField(
        widget=forms.Textarea
    )

    cn = (
        ('', '--Select--'),
        ('bangalore', 'Bangalore'),
        ('chennai', 'Chennai')
    )

    gn = (
        ('m', 'Male'),
        ('f', 'Female')
    )

    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect)
    city = forms.ChoiceField(choices=cn)

    is_Active = forms.CharField(widget=forms.CheckboxInput)
    is_Active_1 = forms.BooleanField()

    file = forms.FileField()

    password = forms.CharField(widget=forms.PasswordInput())


    def clean(self):
        form_data = self.cleaned_data

        if 'username' in form_data and form_data['username'].isdigit():
            self.errors['username']=['Invalid Name']

        if 'email' in form_data and form_data['email'].lower().find('@eainfobiz.com')<0:
            self.errors['email']=['Invalid Email']

        if 'password' in form_data:
            errormsg="""
                At least one upper case,
                At least one lower case,
                At least one digit,
                At least one Special Char,
                Minimum eight in length,
            """
        pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})';
        string=form_data['password']
        matchstring=re.findall(pattern,string)
        if not matchstring:
            self.errors['password']=[errormsg]


        return form_data
