from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
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

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post-detail.html'
	# cargamos el contexto
	context_object_name = 'post'
	# definimos content_data
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		post = Post.objects.filter(slug=self.kwargs.get('slug'))
		return context
