from django.shortcuts import render, redirect

from .models import Experiment

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        
        if username == 'admin':
            return redirect('form1')
        else:
            return redirect('desc')
    else:
        return render(request, 'core/login.html', {})

def form1(request):
    if request.method == 'POST':
        feedback = bool(int(request.POST.get('feedback')))
        all_buttons = bool(int(request.POST.get('all_buttons')))

        experiment = Experiment.objects.create(
            feedback=feedback,
            all_buttons=all_buttons,
        )
        experiment.save()

        return redirect('form2')
    
    else:
        return render(request, 'core/form1.html', {})

def form2(request):
    if request.method == 'POST':
        experiment = Experiment.objects.latest('pk')
        experiment.lighting_time = int(request.POST.get('lighting_time'))
        experiment.interval_time = int(request.POST.get('interval_time'))
        experiment.session_time = int(request.POST.get('session_time'))
        experiment.username = request.POST.get('username')
        experiment.save()

        return redirect('login_page')
    
    else:
        return render(request, 'core/form2.html', {})

def desc(request):
    return render(request, 'core/desc.html', {})

def end_trial(request):
    return render(request, 'core/end_trial.html', {})

def experiment(request):
    pass
