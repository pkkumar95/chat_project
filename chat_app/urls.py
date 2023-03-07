from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rooms/', views.RoomListView.as_view(), name='room-list'),
    path('rooms/create/', views.RoomCreateView.as_view(), name='room-create'),
    path('rooms/<int:pk>/', views.RoomDetailView.as_view(), name='room-detail'),
    path('rooms/<int:pk>/update/', views.RoomUpdateView.as_view(), name='room-update'),
    path('rooms/<int:pk>/delete/', views.RoomDeleteView.as_view(), name='room-delete'),
    path('rooms/<int:pk>/invite/', views.RoomInviteView.as_view(), name='room-invite'),
    path('rooms/<int:pk>/join/', views.RoomJoinView.as_view(), name='room-join'),
    path('messages/', views.MessageListView.as_view(), name='message-list'),
    path('messages/create/', views.MessageCreateView.as_view(), name='message-create'),
    path('profiles/', views.ProfileListView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profiles/<int:pk>/update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('profiles/<int:pk>/delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
