from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import registerForm, editProfileForm, changePasswordForm, createAccountForm
# from django.urls import reverse_lazy, reverse
from django.urls import reverse
from blogApp.models import Profile

class userRegister(generic.CreateView):
    # form_class = registerForm
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    # success_url = 'login'
    def get_success_url(request):
        return reverse('login')


class createAccount(CreateView):
    model = Profile
    form_class = createAccountForm
    template_name = 'registration/create-account.html'
    # fields = "__all__"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class viewProfile(DetailView):
    model = Profile
    template_name = 'registration/profile_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(viewProfile, self).get_context_data(*args, **kwargs)
        current_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['current_user'] = current_user
        return context

# class editProfile(generic.UpdateView):
#     model = Profile
#     # form_class = editForm
#     template_name = "registration/editprofile.html"
#     fields = ['bio','profile_pic']
#     success_url = reverse_lazy('home')
#     #
#     # def get_object(self):
#     #     return self.request.user

class editProfile(generic.UpdateView):
    model = Profile
    # form_class = editForm
    template_name = 'registration/editprofile.html'
    fields = ['bio','profile_pic']
    # success_url = reverse_lazy('home')

class userEditProfile(generic.UpdateView):
    form_class = editProfileForm
    template_name = 'registration/edit-profile.html'
    # success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def get_success_url(request):
        return reverse('home')

class changePasswords(PasswordChangeView):
    form_class = PasswordChangeForm
    # form_class = changePasswordForm
    def get_success_url(request):
        return reverse('password_success')
    # success_url = reverse_lazy('password_success')
    # success_url = reverse_lazy('home')

def password_success(request):
    return render(request, 'registration/password_success.html')
# Create your views here.
