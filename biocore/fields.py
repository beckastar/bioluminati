from django import forms
from django.utils.safestring import mark_safe
from django.db.models.loading import get_model

class UneditableText(forms.TextInput):
    input_type = 'hidden'

    def __init__(self, *args, **kwargs):
        super(UneditableText, self).__init__(*args, **kwargs)
        self.attrs = kwargs.get('attrs', {})
        self.text = self.attrs.get('text', False)
        
    def render(self, name, value, *args, **kwargs):
        text = self.text
        html = '%s %s' % (super(UneditableText, self).render(name, value, self.attrs), text)
        return mark_safe(html)