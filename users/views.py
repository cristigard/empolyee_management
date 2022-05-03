from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib import messages
from .admin import UserCreationForm
from .forms import UserUpdateForm, CustomLoginForm, CustomUserPasswordChangeForm, CustomUserPasswordResetForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin




def home(request):
	return render(request, 'users/home.html')


class UserSignUpView(SuccessMessageMixin, CreateView):
	template_name = 'users/signup.html'
	form_class = UserCreationForm
	success_message = "Profile was created successfully."
	success_url = reverse_lazy('login')

	#redirect authenticated users
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('employee-list')
		return super().dispatch(request, *args, **kwargs)


@login_required()
def profile(request):
	form = UserUpdateForm(instance = request.user)
	if request.method == "POST":
		form = UserUpdateForm(request.POST, request.FILES, instance = request.user)
		if form.is_valid():
			form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
	else:
		form = UserUpdateForm(instance = request.user)
	return render(request, 'users/profile.html', {'form':form})


class UserLoginView(SuccessMessageMixin, LoginView):
	authentication_form = CustomLoginForm
	template_name = 'users/login.html'
	redirect_authenticated_user = True
	success_message = "Login successfully." 

	def get_success_url(self): # + redirect_authenticated_user = True -> send to other view if user is already auth and try to access login page
		return reverse_lazy('employee-list')


class UserLogoutView(SuccessMessageMixin, LogoutView):
	next_page = 'login'
	success_message = "Logout successfully" 


class UserChangePassView(LoginRequiredMixin, PasswordChangeView):  
	form_class = CustomUserPasswordChangeForm
	template_name = 'users/password_change_form.html'
	success_url = reverse_lazy('password_change_done')

class UserChangePassDoneView(LoginRequiredMixin, PasswordChangeDoneView):
	template_name = 'users/password_change_done.html'

