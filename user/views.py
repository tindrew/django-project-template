from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

@login_required(login_url='user-login')
def user_dashboard(request):
    
    return render(request, 'user/user-dashboard.html')