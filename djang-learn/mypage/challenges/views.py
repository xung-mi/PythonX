from django.shortcuts import render
from django.http import (
    Http404,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None,
}


# Create your views here.
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    """
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
    """
    return render(
        request,
        "challenges/index.html",
        {"months": months},
    )


def monthly_challenge_by_number(request, month):
    month_text_keys = monthly_challenges.keys()
    months = list(month_text_keys)

    if 1 <= month <= 12:
        redirect_month = months[month - 1]
    else:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)

    """
        month-challenge is name defined in urls.py
        redirect là gọi reverse ngầm, cho phép sent request to another page
        để tránh hard-code cho:
            return HttpResponseRedirect("/challenges/" + redirect_month)
        thì dùng reverse
    """
    redirect_path = reverse(
        "month-challenge", args=[redirect_month]
    )  # /challenge/ + january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    # Sử dụng .get() để tránh lỗi KeyError nếu tháng không tồn tại
    text_month = monthly_challenges.get(month)

    # Kiểm tra xem text_month có phải là None không (bao gồm cả trường hợp tháng không tồn tại và tháng 12)
    if text_month is None:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
        # return Http404()
    else:
        # Nếu text_month có giá trị, render template challenge.html như bình thường
        return render(
            request,
            "challenges/challenge.html",
            {"text": text_month, "month_name": month},
        )
