from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Snippet
from django.core.validators import RegexValidator

from myapp.models import Snippet

# class NameWidget(forms.MultiWidget):
#     def _init__(self, attrs=None):
#         super().__init__([
#             forms.TextInput(),
#             forms.TextInput()
#         ],attrs)
    
#     def decompress(self, value):
#         if value:
#             return value.split('')
#         return ['first name','last name']

# class NameField(forms.MultiValueField):
#     widget = NameWidget
    
#     def __init__(self,*args,**kwargs):
        
#         fields=(
#             forms.CharField(validators=[RegexValidator(r'[a-zA-Z]+', 'Enter a valid first name')]),
#             forms.CharField(validators=[RegexValidator(r'[a-zA-Z]+', 'Enter a valid last name')])
#         )
        
#         super().__init__(fields, *args, **kwargs)
    
#     def compress(self, data_list):
#         # data_list = ['firstvalue', 'secondvalue']
#         return f'{data_list[0]} {data_list[1]}'
#         #'firstvalue' 'secondvalue'

# class Contactform(forms.Form):
#     name = forms.CharField(max_length=20)
#     email = forms.EmailField(label="email")
#     catagory = forms.ChoiceField(choices = [('question' , 'Questions'),('other','Other')])
#     subject = forms.CharField(required=False)
#     body = forms.CharField(widget=forms.Textarea)
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         self.helper = FormHelper
#         self.helper.form_method = 'post'
       
        
#         self.helper.layout = Layout(
#             'name',
#             'email',
#             'p_num',
#             'body',
#             Submit('submit', 'Submit', css_class='btn-success')
#         )
        
    
class SnippitForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(label="email")
    p_num = forms.CharField(max_length=10)
    body = forms.CharField(widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper
        self.helper.form_method = 'post'
       
        
        self.helper.layout = Layout(
            'name',
            'email',
            'p_num',
            'body',
            Submit('submit', 'Submit', css_class='btn-success')
        )
    
    class Meta:
        model = Snippet
        fields = ('name','email','p_num','body')