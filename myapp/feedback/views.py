from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from . models import Feedback
from django.urls import reverse

def index(request):
	return HttpResponse("Default landing page for feedback");

def requestFeedback(request, feedback_id):
	feedback = get_object_or_404(Feedback, pk=feedback_id)
	return render(request, 'feedback/showFeedback.html', {'feedback':feedback})

def submit(request, feedback_id):
	feedback = get_object_or_404(Feedback, pk=feedback_id)
	try: 
		feedback.stars = request.POST.get('noOfStars')
		feedback.comments = request.POST.get('commenttextarea')
		feedback.save()
		print(feedback.stars)
		print(feedback.comments)
		return HttpResponse('Successfully submitted')
	except(KeyError, Feedback.DoesNotExist):
		return HttpResponse('Error')