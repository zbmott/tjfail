from django import forms

from tjfail.models import Fail


class FailSubmissionForm(forms.ModelForm):
    class Meta:
        model = Fail
        fields = ['body', 'year', 'favorite_teacher']
        labels = {
            'body': 'Your message',
            'year': 'Graduation year'
        }
        help_texts = {
            'favorite_teacher': 'To prove you really went to TJ.'
        }
