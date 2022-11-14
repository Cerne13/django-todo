from django.utils import timezone

from django import forms
from django.core.exceptions import ValidationError

from todo.models import Task, Tag


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"


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
        widget=DateTimeInput(),
    )

    class Meta:
        model = Task
        fields = (
            "content",
            "deadline",
            "done",
            "tags",
        )

    # made validation after the deadline - just for myself
    # there is a problem with timezone - trying to fix +- 2 hour diff between UTC and local :(
    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]

        if deadline:
            print(deadline)
            now = timezone.now()
            print(now)

            if deadline <= now:
                raise ValidationError("Deadline cannot be earlier than current date and time")

        return deadline
