from django.shortcuts import render
from .models import Partner, TeamMember, News, HistoryLine, HistoryDetail, Contacts, Organizer, MainPageNews, HistoryLineMain

def index(request):
    main_news = MainPageNews.objects.select_related("news").order_by("order")
    history_line = HistoryLineMain.objects.filter(is_active=True).first()  
    partners = Partner.objects.all()
    organizers = Organizer.objects.all()

    return render(request, 'main.html', {
        'main_news': main_news,
        'history_line': history_line,  
        'partners': partners,
        'organizers': organizers,
    })

def news_page(request):
    main_news = News.objects.filter(is_main=True).first()
    other_news = News.objects.exclude(id=main_news.id) if main_news else News.objects.all()

    news_per_page = 9
    news_with_page = []
    for idx, news in enumerate(other_news):
        page = idx // news_per_page + 1
        news_with_page.append({
            "news": news,
            "page": page
        })

    total_pages = (len(other_news) + news_per_page - 1) // news_per_page
    page_numbers = list(range(1, total_pages + 1))

    return render(request, "news.html", {
        "main_news": main_news,
        "news_with_page": news_with_page,
        "page_numbers": page_numbers,
    })

def main_page(request):
    history_line = HistoryLineMain.objects.filter(is_active=True).first() 
    return render(request, "index.html", {
        "history_line": history_line
    })

def team_page(request):
    team_list = TeamMember.objects.all()
    return render(request, "teams.html", {"team_members": team_list})

def partners_page(request):
    organizers = Organizer.objects.all()
    partners = Partner.objects.all()
    return render(request, 'partners.html', {'organizers': organizers, 'partners': partners})

def history_lines_page(request):
    lines = HistoryLine.objects.all().order_by('order')
    return render(request, 'historyLine.html', {'history_lines': lines})

def contacts_page(request):
    contacts = Contacts.objects.first() if hasattr(Contacts, 'objects') else None
    return render(request, "contacts.html", {"contacts": contacts})
