from django import forms

from . models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Task
        exclude = ["datetime", "done"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
