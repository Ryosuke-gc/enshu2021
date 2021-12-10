from django.shortcuts import render

def init(request):
    params = {
        'content' : 'Hello world!'
    }
    return render(request,'seat_app/index.html',params)

def send_data(request):
    pass # data receive, add to database
    return # success response