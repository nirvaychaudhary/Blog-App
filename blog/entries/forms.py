from django import forms 
from .models import EntryModel
  
class BlogForm(forms.ModelForm): 
  
    class Meta: 
        model = EntryModel
        fields = ['entry_image','entry_title', 'entry_text'] 
