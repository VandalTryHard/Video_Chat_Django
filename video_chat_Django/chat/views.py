from django.shortcuts import render

# Create your views here.

def main_view(request):
    contex ={}
    return render(request, 'chat/main.html', context=contex)