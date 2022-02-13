from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileListSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework import status

def index(request):
    return render(request, 'index.html')

def download(request, uid):
    context = {
        "folder_name": uid
    }
    return render(request, "download.html", context=context)

class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser]
    def post(self, request):
        try:
            serializer = FileListSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
