'''#from django.shortcuts import render
from django.http import JsonResponse
from .models import Consultation


def consultation_create(request):

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        description = request.POST.get("description")

        Consultation.objects.create(
            name=name,
            phone=phone,
            city=city,
            description=description
        )

        return JsonResponse({
            "message": "درخواست شما ثبت شد"
        })

    return JsonResponse({
        "message": "Only POST allowed"
    })
# Create your views here.'''

from django.shortcuts import render
from django.http import JsonResponse
from .models import Consultation


def home(request):
    return render(request, "index.html")


def consultation_create(request):

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        description = request.POST.get("description")

        Consultation.objects.create(
            name=name,
            phone=phone,
            city=city,
            description=description
        )
        return JsonResponse({
    "message": "درخواست شما با موفقیت ثبت شد، کارشناسان SAPWOOD به‌زودی با شما تماس می‌گیرند."
})

    

    return JsonResponse({
        "message": "Only POST allowed"
    })
