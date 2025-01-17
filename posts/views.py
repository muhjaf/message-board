from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Rendering template with context:", context)
        return context