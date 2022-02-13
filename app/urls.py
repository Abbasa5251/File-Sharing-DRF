from django.urls import path
from .views import HandleFileUpload, index, download

urlpatterns = [
    path('', index, name="index"),
    path('download/<uuid:uid>/', download, name="download"),
    path('handle/', HandleFileUpload.as_view(), name="file-upload-handler")
]
