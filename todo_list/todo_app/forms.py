from django import forms
from .models import Task


class AddTaskForm(forms.ModelForm):
    """Форма добавления задачи"""

    class Meta:
        model = Task
        fields = ('title',)