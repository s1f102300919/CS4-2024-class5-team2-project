from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def top(request):
    data = {
        "subject1": "数学",
        "subject_list": ["CS概論", "CS演習", "SW演習", "物理", "数学"]
    }
    return render(request, "index.html", data)