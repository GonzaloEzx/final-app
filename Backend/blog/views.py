from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

# Create your views here.
class BlogHomePageView(TemplateView):
	template_name="blog/index.html"

	# cargamos desde la base de datos.
	# definimos get_context_data - **kwargs / selec toda las categorias.
	def get_context_data(self, **kwargs):
		# siempre se declara un contexto.
		context = super().get_context_data(**kwargs)
		# referencia a nombres de la base de datos.
		context["posts"] = Post.postobjects.all()
		return context
