from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
# Create your views here.
# def register(request):
#     if request.method =='POST':
#         form = RegistrationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             email = request.POST['email']
#             password = request.POST['password1']
#             user = authenticate(request, email=email, password = password)
#             login(request, user)
#             return redirect('blog-home')

#         else:
#             form = RegistrationForm()
#         return redirect('blog-home')
#     form = RegistrationForm(request.POST)
#     return render(request, 'users/register.html', {
#         'form': form
#         })

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             print("Form isn valid")
#             print(form.cleaned_data)
#             user = authenticate(request, email = form.cleaned_data['email'])

#             user.save()
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect('blog-home')
            
#     elif request.method == 'GET':
#         form = RegistrationForm()

#     form = RegistrationForm()
#     return render(request, 'users/register.html', {
#         'form': form
#     })

def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('blog-home')
    context = {'form': form}
    return render(request, "users/register.html", context)