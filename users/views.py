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
            # Show success flash message after redirecting to blog home
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account for {username} created!')
            return redirect('blog-home')
    # Get method ie webpage requested
    else:
        # create new form
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'users/register.html', context)
