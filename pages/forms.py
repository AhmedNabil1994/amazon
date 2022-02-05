from dataclasses import field, fields
from pyexpat import model
from django import forms 
from .models import*


class InsertUsers(forms.Form):
    userName=forms.CharField(max_length=30)
    userEmail=forms.EmailField(widget=forms.EmailInput)
    userPassword=forms.CharField(max_length=12,widget=forms.PasswordInput)

class InsertUsersModel(forms.ModelForm):
    userPassword=forms.CharField(max_length=12,widget=forms.PasswordInput)
    class Meta:
        fields='__all__'
        model=Myusers

class InsertTrainee(forms.Form):
    name = forms.CharField(max_length=40)
    track_id = forms.ChoiceField(choices=[(track.id,track.name)for track in Track.objects.all()])
