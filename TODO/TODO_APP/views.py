from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task


# Create your views here.

class Tasklist(ListView):
    model = Task  # to fetch data from database
    context_object_name = 'task'
    template_name = 'list.html'


class TaskCreate(CreateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('task-create')
    template_name = 'taskcreated.html'

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)


class TaskUpdate(UpdateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('task')
    template_name = 'taskcreated.html'


class TaskDelete(DeleteView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('task')
    template_name = 'taskdelete.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detailview.html'


class CustomLoginView(LoginView):
    fields = '__all__'
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task')


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)                           # this is used for validating the user ie. if user is already
        return super(RegisterView,self).form_valid(form)       # exist then login else register.

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('task')
        return super(RegisterView,self).get(*args,**kwargs)
