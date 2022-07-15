from django.shortcuts import redirect


def home(request):
    return redirect('master_dashboard')
    # return render(request, 'home/index.html')
