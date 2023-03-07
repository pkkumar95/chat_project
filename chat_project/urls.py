from django.urls import path, include

urlpatterns = [
    path('', include('chat_app.urls')),
]
