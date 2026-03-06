from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse,JsonResponse
import boto3
import requests
import uuid
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt



def home(request):
    return render(request,'home.html',{"context":"Hi "})



def upload_image(request):

    if request.method == "POST":

        image = request.FILES.get("image")

        if not image:
            return render(request, "upload.html", {"error": "No image selected"})

        unique_filename = f"uploads/{uuid.uuid4()}_{image.name}"

        s3 = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME
        )

        s3.upload_fileobj(
            image,
            settings.AWS_STORAGE_BUCKET_NAME,
            unique_filename
        )

        file_url = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.{settings.AWS_S3_REGION_NAME}.amazonaws.com/{unique_filename}"

        return render(request, "upload.html", {
            "file_url": file_url
        })

    return render(request, "upload.html")
