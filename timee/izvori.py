from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Headlines, LastFetch
from .views import get_friendly_source_name, get_relative_time 

def prikaz_izvora(request, kljucna_rijec):
    last_updated = LastFetch.get_last_update_time()
    vijesti = Headlines.objects.filter(source__icontains=kljucna_rijec).order_by('-published_date')
    for vijest in vijesti:
        vijest.source_name = get_friendly_source_name(vijest.source)
        vijest.time_since = get_relative_time(vijest.published_date)
    
    items_per_page = 10
    paginator = Paginator(vijesti, items_per_page)
    page = request.GET.get("page")
    try:
        news_page = paginator.page(page)
    except PageNotAnInteger:
        news_page = paginator.page(1)
    except EmptyPage:
        news_page = paginator.page(paginator.num_pages)
    
    context = {
        'naslov_stranice': f'{kljucna_rijec.capitalize()} - Time.ba',
        'vijesti': vijesti,
        'news_page': news_page,
        'last_updated': last_updated,
    }

    return render(request, 'prikaz_izvora.html', context)


def svi_izvori(request):
    last_updated = LastFetch.get_last_update_time()
    context = {
        'naslov_stranice': 'Izvori - Time.ba',
        'last_updated': last_updated,
    }
    return render(request, 'izvori.html', context)
