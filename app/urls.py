from django.urls import path
from .views import HandleFileUpload, index

urlpatterns = [
    path('', index),
    path('handle/', HandleFileUpload.as_view())
]
