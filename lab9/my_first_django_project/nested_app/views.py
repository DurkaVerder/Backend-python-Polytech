from django.http import HttpResponse

def first_view(request):
    return HttpResponse("<h1>First nested view</h1>")

def second_view(request):
    return HttpResponse("<h1>Second nested view</h1>")
