from django.views.generic import TemplateView


# Create your views here.

class HomePageViews(TemplateView):
    template_name = 'base/home.html'


class SobrePageViews(TemplateView):
    template_name = 'base/sobre.html'
