from django import forms
from .models import ToDoList
from ckeditor.fields import RichTextField



class NewTaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Task title'}
        ),
        max_length=100,
        help_text='The max length for title is 100.'
    )
    rich_text = forms.RichTextField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = ToDoList
        fields = ['subject', 'message']
