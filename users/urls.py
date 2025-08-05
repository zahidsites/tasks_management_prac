from django.urls import path
from users.views import sign_up, signIn, logOut


urlpatterns = [
    path('sign-up/',sign_up, name='sign-up'),
    path('signin',signIn, name='signin'),
    path('logOut',logOut, name='logout')
]
