from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateform
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=="POST":
        form =UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username  =form.cleaned_data.get('username')
            messages.success(request,f"Congrats! Your account has been Created. Now You are able to Login!")
            return redirect('login')


    else:
        form =UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


@login_required
def Profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form =  ProfileUpdateform(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)


        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request,'Your Profile has been Updated!')
            return redirect('profile')
        else:
            messages.error(request,'Please fill valid details.!')



    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateform(instance = request.user.profile)

    context = { 'u_form' : u_form ,
                'p_form' : p_form }
    return render(request,'users/profile.html', context)