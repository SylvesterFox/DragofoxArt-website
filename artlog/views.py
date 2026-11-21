from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Artwork, CommissonsStatus




# Прайс-лист: (название группы, [(услуга, цена в USD), ...])
PRICE_GROUPS = [
    ("ILLUSTRATIONS", [
        ("Head — sketch", "4.88"),
        ("Head — color", "6.10"),
        ("Head — shaded", "8.54"),
        ("Bust — sketch", "7.32"),
        ("Bust — color", "9.15"),
        ("Bust — shaded", "10.37"),
        ("Full body — sketch", "9.76"),
        ("Full body — color", "11.59"),
        ("Full body — shaded", "13.42"),
        ("Sticker pack (5 stickers)", "7.93"),
    ]),
    ("EXTRAS", [
        ("Reference sheets", "13.42"),
        ("Background", "2.44"),
        ("Additional characters", "2.44"),
        ("NSFW content", "6.10"),
    ]),
]


def index(request):
    status = CommissonsStatus.objects.first()

    # # Статус комиссий на главной: True -> OPEN (зелёный), False -> CLOSED (красный)
    COMMISSIONS_OPEN = (
        status.commissons_status if status else True
    )
    context = {
        "commissions_open": COMMISSIONS_OPEN,
        "price_groups": PRICE_GROUPS,
        "latest_arts": Artwork.objects.filter(is_published=True)[:6],
    }
    return render(request, "index.html", context)


def gallery(request):
    arts = Artwork.objects.filter(is_published=True)
    return render(request, "artlog/gallery.html", {"arts": arts})


def artwork_detail(request, pk):
    art = get_object_or_404(Artwork, pk=pk, is_published=True)
    return render(request, "artlog/detail.html", {"art": art})

