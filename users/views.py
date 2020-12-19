from django.shortcuts import render, redirect
from django.contrib import messages

from users.forms import UserRegistrationForm

def register(request):
    # Request methos is post ie form submitted
    if request.method == 'POST':
        # create form based on data received in Post req
        form = UserRegistrationForm(request.POST)
        # Check if form is valid
        if form.is_valid():
            # if form is valid then add user to db
            form.save()
            # Redirect to login page and show success msg
            messages.success(request,f'Account created! You can now login')
            return redirect('login')
    # Get method ie webpage requested
    else:
        # create new form
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'users/register.html', context)
