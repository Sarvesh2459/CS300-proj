from django import forms  
class StudentForm(forms.Form):  
    id = forms.CharField(label="Enter ID",max_length=50)
