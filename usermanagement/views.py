from django.shortcuts import render,redirect

from usermanagement.forms import SignUpForm
from django.contrib.auth import login,authenticate


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index_t')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

