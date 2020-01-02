from django.shortcuts import render
# Class based views
from django.views.generic import TemplateView

from django.utils.translation import ugettext as _

# Create your views here.
class HomeView(TemplateView):
    template_name = "generic/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        str_var = _("This string must be translated")
        context['str_var'] = str_var
        context['test'] = "Home view!"
        return context