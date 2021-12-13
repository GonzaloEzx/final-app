from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

# Create your views here.
class BlogHomePageView(TemplateView):
	template_name="blog/index.html"

	# cargamos desde la base de datos.
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["posts"] = Post.postobjects.all()
		return context
