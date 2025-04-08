from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Tháng 1",
    "february": "Tháng 2",
    "march": "Tháng 3",
    "april": "Tháng 4",
    "may": "Tháng 5",
    "june": "Tháng 6",
    "july": "Tháng 7",
    "august": "Tháng 8",
    "september": "Tháng 9",
    "october": "Tháng 10",
    "november": "Tháng 11",
    "december": "Tháng 12",
}

# Create your views here.

def january(request):
    return HttpResponse("Tháng 1")

def february(request):
    return HttpResponse("Tháng 2")

def monthly_challenge_by_number(request, month):
    month_text_keys = monthly_challenges.keys()
    months = list(month_text_keys)
    if 1 <= month <= 12:
        redirect_month = months[month - 1]
    else:
        return HttpResponseNotFound("<h1>Tháng không hợp lệ</h1>")
    
    '''
        month-challenge is name defined in urls.py
        redirect là gọi reverse ngầm
        để tránh hard-code cho:
            return HttpResponseRedirect("/challenges/" + redirect_month)
        thì dùng reverse
    '''
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/ + january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        text_month = monthly_challenges.get(month)
        response_data = f"<h1>{text_month}</h1>"
        return HttpResponse(text_month)
    except:
        if text_month is None:
            return HttpResponseNotFound("<h1>This month is not supported</h1>")
        else:
            return HttpResponseNotFound("<h1>Error</h1>")