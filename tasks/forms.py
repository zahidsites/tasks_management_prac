from tasks.models import Task, TaskDetail
from django import forms

class taskFormModel(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class taskDetailsModel(forms.ModelForm):
    class Meta:
        model = TaskDetail
        fields = ['priority']
