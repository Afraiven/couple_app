from django.http import HttpResponse, JsonResponse
from django.template import loader

from datetime import datetime, date
from .models import Tekst, Daily

def index(request):
    # t = Tekst.objects.all()
    # for x in t:
    #     x.seen = 0
    #     x.opened_date = None
    #     x.save()
    # reset_daily = Daily.objects.get(id=1)
    # reset_daily.counter = 3
    # reset_daily.save()

    opened = Tekst.objects.filter(seen = 1).order_by('-opened_date')

    ile_tekstow = len(Tekst.objects.all())
    ile_widzianych = len(Tekst.objects.filter(seen = 1))
    daily = str(Daily.objects.get(id=1))[8:10]
    today = str(datetime.now())[8:10]

    daily_obj = Daily.objects.get(id=1)
    if (today !=  daily):
        daily_obj.today = datetime.now()
        daily_obj.counter = 3
        daily_obj.save()

    teksty = Tekst.objects.filter(seen = 0).order_by("?")[:9]
    template = loader.get_template('app/index.html')
    context = {
        'ile_tekstow': ile_tekstow,
        'ile_widzianych': ile_widzianych,
        'teksty': teksty,
        'daily_counter': daily_obj.counter,
        'opened': opened,
    }
    return HttpResponse(template.render(context, request))

def decrease_counter(request):
        tekst = Tekst.objects.get(id=request.POST['name'])
        tekst.seen = 1
        tekst.opened_date = date.today()
        tekst.save()
        daily_obj = Daily.objects.get(id=1)
        counter = Daily.objects.get(id=1).counter
        counter_new = counter
        if counter > 0:
            counter_new = counter - 1
            daily_obj.counter = counter - 1
            daily_obj.save()
            
        return JsonResponse({"counter": counter_new})


def show_card(request, code):
    card = Tekst.objects.get(code=code)
    template = loader.get_template('app/card.html')
    context = {
        "card": card,
        "img": card.image,
        "img2": card.image2,
    }
    return HttpResponse(template.render(context, request))
