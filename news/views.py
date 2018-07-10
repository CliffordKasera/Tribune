from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Article

# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')



def news_of_day(request):
    date = dt.date.today()
    news = Article.todays_news()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    # day = convert_dates(date)
    # html = f'''
    #     <html>
    #         <body>
    #             <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
    #         </body>
    #     </html>
    #         '''
    return render(request, 'all-news/today-news.html', {"date": date, "news":news})

def past_days_news(request,past_date):
    # Converts data from the string Url
    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
        # day = convert_dates(date)
        # html = f'''
        #     <html>
        #         <body>
        #             <h1>News for {date.day}-{date.month}-{date.year}</h1>
        #         </body>
        #     </html>
        #         '''
        # return render(request, 'all-news/today-news.html', {'date': date,})
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)
    
    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html', {'date': date,"news":news})
    

