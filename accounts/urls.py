from django.urls import path
from .views import SignUpView, edit_schedule, home, user_schedule

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit-schedule/', edit_schedule, name='edit_schedule'),
    path('', home, name='home'),  # Homepage URL
    path('my-schedule/', user_schedule, name='user_schedule'),  # New URL for user schedule
]