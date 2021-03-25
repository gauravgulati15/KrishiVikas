from django.shortcuts import render

# Create your views here.
def aboutus_list(request):
    context = {}

    return render(request, "aboutus/about.html", context)
