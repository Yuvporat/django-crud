from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from .models import JobOffer
from .serializers import JobOfferSerializer
# Create your views here.
# def job_list_create_api_view():
#     pass
# def JobEditDelete():
#     pass

@api_view(["GET", "POST"])
def job_list_create_api_view(request):

    if request.method == "GET":
        jobs = JobOffer.objects.filter(available=True)
        serializer = JobOfferSerializer(jobs, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def job_detail_api_view(request, pk):
    try:
        job = JobOffer.objects.get(pk=pk)
    except job.DoesNotExist:
        return Response({"error": {
                            "code": 404,
                            "message": "Job not found!"
                        }}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = JobOfferSerializer(job)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = JobOfferSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)