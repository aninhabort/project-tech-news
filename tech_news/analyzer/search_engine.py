from tech_news.database import search_news


#  Requisito 7
def search_by_title(title):
    find = search_news({"title": {"$regex": title, '$options': 'i'}})
    news_by_title = []

    for news in find:
        news_by_title.append((news["title"], news["url"]))

    return news_by_title


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
