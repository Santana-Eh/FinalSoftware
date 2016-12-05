from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


# Create your views here.
def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

@login_required
def userProfile(request):
    user = request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request, template, context)

class UserFormView(View):
    form_class = UserForm
    template_name = "signup.html"


    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    def post(self,request):
        form = self.form_class(request.Post)

        if form.is_valid():
            # creates a a form locally
            user = form.save(commit=False)

            # format properly
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()


            # returns User object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
        return redirect('home.html') # need to check for login profile, user should be redirected to login screen