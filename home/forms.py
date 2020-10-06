from django import forms
from ckeditor.widgets import CKEditorWidget


class MessageForm(forms.Form):

    message_full_name = forms.CharField(max_length=50)
    message_email = forms.EmailField(max_length=254)
    message_phone_number = forms.CharField(max_length=20)
    message_subject = forms.CharField(max_length=60)
    message_body = forms.CharField(widget=CKEditorWidget())

    def __init__(self, *args, **kwargs):
        """Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field."""
        super().__init__(*args, **kwargs)
        placeholders = {
            'message_full_name': 'Full Name',
            'message_email': 'Email Address',
            'message_phone_number': 'Phone Number',
            'message_subject': 'Message Subject',
        }

        for field in self.fields:
            if field != 'message_body':
                placeholder = f'{placeholders[field]} *'
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False
