from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from polling_app.models import voters


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class votersForm(forms.ModelForm):
    class Meta:
        model= voters
        fields = "__all__"
#     voter_name = forms.CharField(max_length=100,  required=True)
#     gender = forms.CharField(max_length=6 , required=True)
#     email = forms.EmailField(max_length=20, required=True)
#     image = forms.ImageField( required=True)
#     phone_number = forms.IntegerField(  required=True)

# class voteForm(forms.Form):
#     voter_name = forms.CharField(max_length=100, required=True)
#     candidate_voted_for = forms.CharField(max_length=100,  required=True)
#     position  = forms.IntegerField(max_length=2, required=True)

# class candidatesForm(forms.Form):
#     candidate_name = forms.CharField(max_length=20,  required=True)
#     gender = forms.CharField(max_length=6,  required=True)
#     image = forms.ImageField(required=True)
#     position = forms.IntegerField( required=True)
#     biography = forms.CharField(max_length=500, required=True)

# class positionForm(forms.Form):
#     candidate_name = forms.CharField(max_length=20, required=True)
#     maximum_votes = forms.IntegerField(max_length=9, required=True)
#     priority = forms.IntegerField(max_length=2, required=True)

# class add_voterForm(forms.Form):
#     voter_name = forms.CharField(max_length=100,  required=True)
#     gender = forms.CharField(max_length=6, required=True)
#     email = forms.EmailField(max_length=20, required=True)
#     image = forms.ImageField( required=True)
#     phone_number = forms.IntegerField(max_length=9,  required=True)

# class add_candidateForm(forms.Form):
#     candidate_name = forms.CharField(max_length=20,  required=True)
#     gender = forms.CharField(max_length=6, required=True)
#     image = forms.ImageField(required=True)
#     position = forms.IntegerField(max_length=2, required=True)
#     biography = forms.CharField(max_length=500, required=True)
