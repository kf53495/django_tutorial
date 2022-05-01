from django.views.generic import TemplateView #htmlをそのまま返す

class IndexView(TemplateView):
    template_name = 'index.html'