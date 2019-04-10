from django import forms
from testapp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        #OR
        #fields = ('emp_nam','emp_email','emp_address')  #//using this we we will create fields which we want
        #fields = ('emp_nam','emp_email')  #// we want emp_nam or emp_addrress