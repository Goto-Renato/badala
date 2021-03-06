from django.contrib.auth.models import User
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'badala/index.html'
    context_object_name = 'all_users'

    def get_queryset(self):
        return User.objects.all()

class DetailView(generic.DetailView):
    model = User
    template_name = 'badala/detail.html'

class UserFormView(View):
    form_class = UserForm
    template_name = 'badala/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('badala:detail', pk=user.id)

        return render(request, self.template_name, {'form': form})











