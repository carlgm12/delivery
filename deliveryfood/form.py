from django import forms
from deliveryfood.models import MenuDay
from datetime import datetime


class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuDay

        now = datetime.now()

        fields = [
            "options",
            "salad",
            "dateMenu",
            "UserLevelID",
        ]

        labels = {
            "options": "options",
            "salad": "salad",
            "dateMenu": "dateMenu",
            "UserLevelID": "UserLevelID",
        }

        widgets = {
            "options": forms.TextInput(attrs={"class": "form-control"}),
            "salad": forms.TextInput(attrs={"class": "form-control"}),
            "dateMenu": forms.TextInput(attrs={"value": now}),
            "UserLevelID": forms.TextInput(attrs={"value": 1, "size": 10}),
        }
