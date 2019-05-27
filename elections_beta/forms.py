from django import forms
from .models import Candidate, Student

class VoteForm(forms.Form):
    stu_name = forms.CharField(widget=forms.TextInput(attrs={'required' : True}), label="Please enter your name:")
    if Candidate.objects.filter(canid=1).exists():
        can1 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkfn'}), label=Candidate.objects.get(canid=1).can_name)
    if Candidate.objects.filter(canid=2).exists():
        can2 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkfn'}), label=Candidate.objects.get(canid=2).can_name)
    if Candidate.objects.filter(canid=3).exists():
        can3 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkfn'}), label=Candidate.objects.get(canid=3).can_name)
    if Candidate.objects.filter(canid=4).exists():
        can4 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkfn'}), label=Candidate.objects.get(canid=4).can_name)
    if Candidate.objects.filter(canid=5).exists():
        can5 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkfn'}), label=Candidate.objects.get(canid=5).can_name)
    if Candidate.objects.filter(canid=6).exists():
        can6 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkfn'}), label=Candidate.objects.get(canid=6).can_name)
    if Candidate.objects.filter(canid=7).exists():
        can7 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkfn'}), label=Candidate.objects.get(canid=7).can_name)
    if Candidate.objects.filter(canid=8).exists():
        can8 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkfn'}), label=Candidate.objects.get(canid=8).can_name)
    if Candidate.objects.filter(canid=9).exists():
        can9 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkfn'}), label=Candidate.objects.get(canid=9).can_name)
    if Candidate.objects.filter(canid=10).exists():
        can10 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkfn'}), label=Candidate.objects.get(canid=10).can_name)
    if Candidate.objects.filter(canid=11).exists():
        can11 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkfn'}), label=Candidate.objects.get(canid=11).can_name)
    if Candidate.objects.filter(canid=12).exists():
        can12 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkfn'}), label=Candidate.objects.get(canid=12).can_name)
    if Candidate.objects.filter(canid=13).exists():
        can13 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkfn'}), label=Candidate.objects.get(canid=13).can_name)
    if Candidate.objects.filter(canid=14).exists():
        can14 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkfn'}), label=Candidate.objects.get(canid=14).can_name)
    if Candidate.objects.filter(canid=15).exists():
        can15 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkfn'}), label=Candidate.objects.get(canid=15).can_name)
