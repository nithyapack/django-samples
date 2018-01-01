from django.urls import path
from . import views

app_name='feedback'
urlpatterns = [
	path('', views.index, name='index'),
	path('requestfeedback/<feedback_id>', views.requestFeedback, name='requestFeedback'),
	path('submit/<feedback_id>', views.submit, name='submit'),
]