from django.shortcuts import render
from django.views import View

# Create your views here.


class index(View):
    def get(self, request):
        return render(request, "main/index.html")

class page_1(View):
    def get(self, request):
        return render(request, "main/page.html", context={'page': 'Page 1'})
    
class page_1_1(View):
    def get(self, request):
        return render(request, "main/page.html", context={'page': 'Page 1.1'})
    
class page_1_1_1(View):
    def get(self, request):
        return render(request, "main/page.html", context={'page': 'page 1.1.1'})
    
class page_1_1_2(View):
    def get(self, request):
        return render(request, "main/page.html", context={'page': 'page 1.1.2'})
    
class page_1_2(View):
    def get(self, request):
        return render(request, "main/page.html", context={'page': 'Page 1.2'})
    
class page_2(View):
    def get(self, request):
        return render(request, "main/page.html", context={'page': 'Page 2'})
    
class page_3(View):
    def get(self, request):
        return render(request, "main/page.html", context={'page': 'Page 3'})
    
class sub_page_1(View):
    def get(self, request):
        return render(request, "main/page.html", context={'page': 'Sub page 1'})
    
class sub_page_2(View):
    def get(self, request):
        return render(request, "main/page.html", context={'page': 'Sub page 2'})
    
class sub_page_1_1(View):
    def get(self, request):
        return render(request, "main/page.html", context={'page': 'Sub page 1.1'})
    
class sub_page_1_1_1(View):
    def get(self, request):
        return render(request, "main/page.html", context={'page': 'Sub page 1.1.1'})