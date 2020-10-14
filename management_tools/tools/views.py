from django.views import View
from django.views.generic.base import HttpResponse


class MainPageView(View):
    def get(self, request):
        return HttpResponse("Main Page")