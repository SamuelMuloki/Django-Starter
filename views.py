from django.shortcuts import render
import re
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, Falcon 9!")

def falcon_launch(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there falcon, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)

def falcon_launch_simplified(request, name):
    return render(
        request,
        'falcon/falcon_launch.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
