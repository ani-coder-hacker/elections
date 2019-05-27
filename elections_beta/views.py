from django.shortcuts import render, redirect
from django.db import IntegrityError
from .forms import VoteForm
from .models import Candidate, Student
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def home(request):
    args = {}
    return render(request, 'elections_beta/home.html', args)

@login_required
def vote(request):

    if Student.objects.filter(stuid=request.user.id).exists():
        return render(request, 'elections_beta/error.html')

    votes = []
    if request.method == 'POST':
        if Candidate.objects.filter(canid=1).exists():
            if request.POST.get('can1', False):
                x = Candidate.objects.get(canid=1)
                x.can_votes += 1
                x.save()
                votes.append(1)

        if Candidate.objects.filter(canid=2).exists():
            if request.POST.get('can2', False):
                x = Candidate.objects.get(canid=2)
                x.can_votes += 1
                x.save()
                votes.append(2)

        if Candidate.objects.filter(canid=3).exists():
            if request.POST.get('can3', False):
                x = Candidate.objects.get(canid=3)
                x.can_votes += 1
                x.save()
                votes.append(3)

        if Candidate.objects.filter(canid=4).exists():
            if request.POST.get('can4', False):
                x = Candidate.objects.get(canid=4)
                x.can_votes += 1
                x.save()
                votes.append(4)

        if Candidate.objects.filter(canid=5).exists():
            if request.POST.get('can5', False):
                x = Candidate.objects.get(canid=5)
                x.can_votes += 1
                x.save()
                votes.append(5)

        if Candidate.objects.filter(canid=6).exists():
            if request.POST.get('can6', False):
                x = Candidate.objects.get(canid=6)
                x.can_votes += 1
                x.save()
                votes.append(6)

        if Candidate.objects.filter(canid=7).exists():
            if request.POST.get('can7', False):
                x = Candidate.objects.get(canid=7)
                x.can_votes += 1
                x.save()
                votes.append(7)

        if Candidate.objects.filter(canid=8).exists():
            if request.POST.get('can8', False):
                x = Candidate.objects.get(canid=8)
                x.can_votes += 1
                x.save()
                votes.append(8)

        if Candidate.objects.filter(canid=9).exists():
            if request.POST.get('can9', False):
                x = Candidate.objects.get(canid=9)
                x.can_votes += 1
                x.save()
                votes.append(9)

        if Candidate.objects.filter(canid=10).exists():
            if request.POST.get('can10', False):
                x = Candidate.objects.get(canid=10)
                x.can_votes += 1
                x.save()
                votes.append(10)

        if Candidate.objects.filter(canid=11).exists():
            if request.POST.get('can11', False):
                x = Candidate.objects.get(canid=11)
                x.can_votes += 1
                x.save()
                votes.append(11)

        if Candidate.objects.filter(canid=12).exists():
            if request.POST.get('can12', False):
                x = Candidate.objects.get(canid=12)
                x.can_votes += 1
                x.save()
                votes.append(12)

        if Candidate.objects.filter(canid=13).exists():
            if request.POST.get('can13', False):
                x = Candidate.objects.get(canid=13)
                x.can_votes += 1
                x.save()
                votes.append(13)

        if Candidate.objects.filter(canid=14).exists():
            if request.POST.get('can14', False):
                x = Candidate.objects.get(canid=14)
                x.can_votes += 1
                x.save()
                votes.append(14)

        if Candidate.objects.filter(canid=15).exists():
            if request.POST.get('can15', False):
                x = Candidate.objects.get(canid=15)
                x.can_votes += 1
                x.save()
                votes.append(15)
        stu_instance = Student.objects.create(stuid=request.user.id, stu_name=request.POST.get('stu_name'), vote1=votes[0], vote2=votes[1], vote3=votes[2], vote4=votes[3], vote5=votes[4], vote6=votes[5])
        return redirect('/logout')
    else:
        form = VoteForm()
        args = {'form' : form}
        return render(request, 'elections_beta/vote.html', args)

@user_passes_test(lambda u: u.is_superuser)
def count(request):

    args = {}

    if Candidate.objects.filter(canid=1).exists():
        can1 = Candidate.objects.get(canid=1)
        args['can1'] = can1
    if Candidate.objects.filter(canid=2).exists():
        can2 = Candidate.objects.get(canid=2)
        args['can2'] = can2
    if Candidate.objects.filter(canid=3).exists():
        can3 = Candidate.objects.get(canid=3)
        args['can3'] = can3
    if Candidate.objects.filter(canid=4).exists():
        can4 = Candidate.objects.get(canid=4)
        args['can4'] = can4
    if Candidate.objects.filter(canid=5).exists():
        can5 = Candidate.objects.get(canid=5)
        args['can5'] = can5
    if Candidate.objects.filter(canid=6).exists():
        can6 = Candidate.objects.get(canid=6)
        args['can6'] = can6
    if Candidate.objects.filter(canid=7).exists():
        can7 = Candidate.objects.get(canid=7)
        args['can7'] = can7
    if Candidate.objects.filter(canid=8).exists():
        can8 = Candidate.objects.get(canid=8)
        args['can8'] = can8
    if Candidate.objects.filter(canid=9).exists():
        can9 = Candidate.objects.get(canid=9)
        args['can9'] = can9
    if Candidate.objects.filter(canid=10).exists():
        can10 = Candidate.objects.get(canid=10)
        args['can10'] = can10
    if Candidate.objects.filter(canid=11).exists():
        can11 = Candidate.objects.get(canid=11)
        args['can11'] = can11
    if Candidate.objects.filter(canid=12).exists():
        can12 = Candidate.objects.get(canid=12)
        args['can12'] = can12
    if Candidate.objects.filter(canid=13).exists():
        can13 = Candidate.objects.get(canid=13)
        args['can13'] = can13
    if Candidate.objects.filter(canid=14).exists():
        can14 = Candidate.objects.get(canid=14)
        args['can14'] = can14
    if Candidate.objects.filter(canid=15).exists():
        can15 = Candidate.objects.get(canid=15)
        args['can15'] = can15

    return render(request, 'elections_beta/count.html', args)
