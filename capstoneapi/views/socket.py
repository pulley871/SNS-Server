from django.views import View
from django.shortcuts import render
class Index(View):
    def get(self, request):
        context = {
            "count": "Hello World"
        }
        return render(request, 'counter/index.html', context)