from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Part

# Create your views here.


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def home(request):
    return render(request, 'home.html')


@login_required
def parts_index(request):
    parts = Part.objects.all()
    return render(request, 'parts/index.html', {'parts': parts})


@login_required
def parts_detail(request, part_id):
    part = Part.objects.get(id=part_id)
    return render(request, 'parts/detail.html', {'part': part})


class PartCreate(LoginRequiredMixin, CreateView):
    model = Part
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PartUpdate(LoginRequiredMixin, UpdateView):
    model = Part
    fields = '__all__'


class PartDelete(LoginRequiredMixin, DeleteView):
    model = Part
    success_url = '/parts/'
