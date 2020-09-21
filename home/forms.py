from django import forms
from ckeditor.widgets import CKEditorWidget


class MessageForm(forms.Form):

    full_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    phone_number = forms.CharField(max_length=20)
    message_subject = forms.CharField(max_length=60)
    message_body = forms.CharField(widget=CKEditorWidget())

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'message_subject': 'Message Subject',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'message_body':
                placeholder = f'{placeholders[field]} *'
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False
