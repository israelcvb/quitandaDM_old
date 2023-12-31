from django.views.generic import TemplateView


# Create your views here.

class HomePageViews(TemplateView):
    template_name = 'base/home.html'
