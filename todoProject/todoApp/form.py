from django import forms

class TodoForm(forms.Form):
    Text = forms.CharField (max_length = 40, widget=forms.TextInput( attrs={"class":"form-control", "placeholder": "Enter todo e.g. Delete junk files", "aria-label": "Todo"}))
   