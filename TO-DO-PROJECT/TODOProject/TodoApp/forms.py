from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'completed'] 

    
    name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Task Name', 'class': 'form-control'}),
        label='Task Name'
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Task Description', 'class': 'form-control', 'rows': 4}),
        label='Description'
    )
    completed = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(),
        label='Completed'
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('Task name is required.')
        return name
