from django.shortcuts import render
from django.views import generic as views

from tasty.accounts.models import Profile

def get_profile(request):
    pass
class IndexView(views.TemplateView):
    template_name = 'home-page.html'

    def get(self, request, *args, **kwargs):
        profile = get_profile(request)
        context = {'profile': profile}
        return render(request, self.template_name, context)