from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

def hello_world(request, name='World'):
    age = request.GET.get('age')
    response_text = f"<h1>Hello, {name}!</h1>"
    if age:
        response_text = f"<h1>Hello, {name}! You are {age} years old.</h1>"
    response = HttpResponse(response_text)
    response.set_cookie('username', name)
    return response

def my_redirect(request):
    return redirect('hello', 'Redirect')

def json(request):
    data = {'name': 'Timur', 'age': 20, "status": "student"}
    return JsonResponse(data)

def show_cookies(request):
    cookies = request.COOKIES
    return HttpResponse(f"<h1>Cookies: {cookies}</h1>")
