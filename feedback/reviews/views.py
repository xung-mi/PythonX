from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReviewSerializer

# Create your views here.

def review(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # Process the form data here
        return render(request, 'reviews/thank_you.html')
    return render(request, 'reviews/review.html')

def thank_you(request):
    return render(request, 'reviews/thank_you.html')

@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        # Return a list of all reviews
        return Response({"message": "List of reviews"})
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            # Save the review data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk):
    if request.method == 'GET':
        # Return a specific review
        return Response({"message": f"Review {pk}"})
    
    elif request.method == 'PUT':
        # Update a review
        return Response({"message": f"Updated review {pk}"})
    
    elif request.method == 'DELETE':
        # Delete a review
        return Response(status=status.HTTP_204_NO_CONTENT)
