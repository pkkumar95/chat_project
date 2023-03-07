from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from .models import ChatRoom, Message, UserProfile
from .forms import RoomForm, MessageForm, ProfileForm, SignUpForm


@method_decorator(login_required, name='dispatch')
class RoomListView(ListView):
    model = ChatRoom
    context_object_name = 'rooms'


@method_decorator(login_required, name='dispatch')
class RoomDetailView(DetailView):
    model = ChatRoom
    context_object_name = 'room'


@method_decorator(login_required, name='dispatch')
class RoomCreateView(LoginRequiredMixin, CreateView):
    model = ChatRoom
    form_class = RoomForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user.profile
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class RoomUpdateView(LoginRequiredMixin, UpdateView):
    model = ChatRoom
    form_class = RoomForm


@method_decorator(login_required, name='dispatch')
class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = ChatRoom
    success_url = reverse_lazy('room-list')


@method_decorator(login_required, name='dispatch')
class RoomInviteView(LoginRequiredMixin, UpdateView):
    model = ChatRoom
    fields = ('invited_users',)
    template_name_suffix = '_invite_form'

    def get_success_url(self):
        messages.success(self.request, 'Invitations sent successfully')
        return super().get_success_url()


@method_decorator(login_required, name='dispatch')
class RoomJoinView(LoginRequiredMixin, UpdateView):
    model = ChatRoom
    fields = ()

    def get_success_url(self):
        messages.success(self.request, 'You have joined the room successfully')
        return super().get_success_url()

    def form_valid(self, form):
        self.object.users.add(self.request.user.profile)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class MessageListView(ListView):
    model = Message
    context_object_name = 'messages'


@method_decorator(login_required, name='dispatch')
class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm

    def form_valid(self, form):
        form.instance.sender = self.request.user.profile
        form.instance.room_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('room-detail', kwargs={'pk': self.kwargs['pk']})


@method_decorator(login_required, name='dispatch')
class ProfileListView(ListView):
    model = UserProfile
    context_object_name = 'profiles'


@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = UserProfile
    context_object_name = 'profile'


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return self.request.user.profile


@method_decorator(login_required, name='dispatch')
class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserProfile
    success_url = reverse_lazy('profile-list')

    def get_object(self, queryset=None):
        return self.request.user.profile
    

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            # Log the user in.
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})