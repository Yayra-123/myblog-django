from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import Userform,ProfileForm

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('post:index')
        
    if request.method == "POST":
        form =Userform(request.POST)
        profile_form =ProfileForm(request.POST)
        
        if form.is_valid() and profile_form.is_valid():
            user=form.save(commit=False)
            
            profile = profile_form.save(commit=False)
            profile.user =user
            
            user.save()
            profile.save()
            return redirect('accounts:login')
            
    else:
        form =Userform()
        profile_form =ProfileForm()
        
    
        
    context={
        'form':form,
        'profile':profile_form,
    }
    return render(request,'account/register.html',context)

def sign_up(request):
    return render(request,'account/logout.html')