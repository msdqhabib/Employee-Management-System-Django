from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname','mobile','emp_code','position')
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'EMP. Code'
        }
    #Insead of .... sequence to use select Text in Possition field
    def __init__(self, *arg, **kwargs):
        super(EmployeeForm, self).__init__(*arg, **kwargs)
        self.fields['position'].empty_lablel = "Select"

        # To exclude fields as requeired field
        # self.fields['emp_code'].required = False