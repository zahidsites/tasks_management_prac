from django.urls import path
from tasks.views import demo

urlpatterns = [
    path('demo', demo, name='demo')
]