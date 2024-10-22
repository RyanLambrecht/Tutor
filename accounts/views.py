from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import TutorCreationForm, TutorChangeForm
from django.contrib.auth.decorators import login_required
from .models import Tutor

class SignUpView(generic.CreateView):
    form_class = TutorCreationForm
    success_url = reverse_lazy('login')  # Redirect to the login page after signup
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

@login_required
def edit_schedule(request):
    if request.method == 'POST':
        form = TutorChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page or any other existing page
    else:
        form = TutorChangeForm(instance=request.user)
    return render(request, 'edit_schedule.html', {'form': form})

def home(request):
    tutors = request.Tutor.objects.all()
    return render(request, 'home.html', {'tutors': tutors})

@login_required
def user_schedule(request):
    user = request.user
    return render(request, 'user_schedule.html', {'user': user})