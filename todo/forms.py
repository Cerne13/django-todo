from datetime import datetime

from django import forms

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    content = forms.CharField(
        max_length=63,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Enter a name for new task"}),
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    deadline = forms.DateTimeField(
        input_formats="%Y-%m-%d %H:%M",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Enter time in format: 'yyyy-mm-dd hh:mm'"})
    )

    class Meta:
        model = Task
        fields = (
            "content",
            "deadline",
            "done",
            "tags",
        )
