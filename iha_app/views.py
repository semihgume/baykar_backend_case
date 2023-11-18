from django.shortcuts import render


def login_page(request):
    return render(request, 'login_page.html')

def register_page(request):
    return render(request, 'register_page.html')

def admin_login_page(request):
    return render(request, 'admin_login_page.html')

def dashboard_page(request):
    cookies = request.COOKIES
    if 'adminToken' in cookies:
        return render(request, 'admin_dashboard.html')
    else:
        return render(request, '401.html')

def uavs_page(request):
    cookies = request.COOKIES
    if 'adminToken' in cookies:
        return render(request, 'uavs.html')
    else:
        return render(request, '401.html')

def rented_uavs_page(request):
    cookies = request.COOKIES
    if 'adminToken' in cookies:
        return render(request, 'rented_uavs.html')
    else:
        return render(request, '401.html')

def home_page(request):
    cookies = request.COOKIES
    print(cookies)
    if 'token' in cookies or 'adminToken' in cookies:
        return render(request, 'home_page.html')
    else:
        return render(request, 'login_page.html')

def profile_page(request):
    cookies = request.COOKIES
    if 'token' in cookies or 'adminToken' in cookies:
        return render(request, 'profile.html')
    else:
        return render(request, '401.html')

