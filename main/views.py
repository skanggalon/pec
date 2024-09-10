from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name_aplication': 'Pacil Electronic Center Depok',
        'name': 'Muhammad Zaid Ats Tsabit',
        'npm' : '2306224410',
        'class': 'PBP D'
    }
    return render(request, "main.html", context)
