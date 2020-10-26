from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.views.generic.edit import CreateView, FormMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.
def product_list(request):
    posts = Post.objects.all()
    return render(request,
                  'posts/list.html',
                  {'posts': posts})

class product_detail(FormMixin, DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'get_post'
    success_url = '/'
    form_class = CommentForm

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['comments'] = Comment.objects.all().order_by('-create_date')
        return context

    def post(self,request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class MyprojectLoginView(LoginView):
    template_name = 'posts/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('main:list')
    def get_success_url(self):
        return self.success_url

class RegisterUserView(CreateView):
    model = User
    template_name = 'posts/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:list')
    success_msg = 'Пользователь успешно создан'
    def form_valid(self,form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username,password=password)
        login(self.request, aut_user)
        return form_valid

class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('main:list')
