from tech_news.database import search_news
from datetime import datetime


#  Requisito 7
def search_by_title(title):
    find = search_news({"title": {"$regex": title, '$options': 'i'}})
    news_by_title = []

    for news in find:
        news_by_title.append((news["title"], news["url"]))

    return news_by_title


# Requisito 8
def search_by_date(date):
    try:
        date_formater = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        find = search_news({"timestamp": date_formater})
        news_by_date = []

        for news in find:
            news_by_date.append((news["title"], news["url"]))
        return news_by_date

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
