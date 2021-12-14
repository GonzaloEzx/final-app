from django.urls import path
from .views import (
	BlogHomePageView,
	PostDetailView,
)

app_name='blog'

urlpatterns = [
	path('', BlogHomePageView.as_view(), name='home'),
	path('<slug>:<pk_slug>/', PostDetailView.as_view(), name='post-detail'),
]