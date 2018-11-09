#importing forms
from django import forms 
 
#creating our forms
class RegisterForm(forms.Form):
 #django gives a number of predefined fields
 #CharField and EmailField are only two of them
 #go through the official docs for more field details
 eloquacdoname = forms.CharField(label='Eloqua Cdo Name', max_length=100)
 hadooptablename = forms.CharField(label='Hadoop Table Name', max_length=100)
 cecid = forms.EmailField(label='Cec Id', max_length=100)
