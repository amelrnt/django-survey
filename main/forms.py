from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from .models import (Discussion, FileAttachment
                    )
from crispy_forms.bootstrap import  FieldWithButtons, StrictButton

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ("name", "phone_number", 
                "question_type", "assigned_user", "question")
        
class GeneralInfoForm(forms.Form):
    keyword = forms.CharField(max_length=255, label="Cari berdasarkan Kata kunci")
    helper = FormHelper()
    helper.form_method = 'POST'

    helper.layout = Layout(
        FieldWithButtons('keyword', StrictButton('Cari!', type='submit', css_class="btn-primary")),
    )

class FileAttachmentForm(forms.ModelForm):
    class Meta:
        model = FileAttachment
        fields = ['file']