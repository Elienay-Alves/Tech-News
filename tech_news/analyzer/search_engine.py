from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    search = {"title": {"$regex": f"{title}", "$options": "i"}}
    result = search_news(search)
    return [(news["title"], news["url"]) for news in result]


# Requisito 8
def search_by_date(date):
    """try:
        date = datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Data Inválida")

    format_date = date.strftime("%d/%m/%Y")
    search = {"timestamp": format_date}

    result = search_news(search)

    return [(news["title"], news["url"]) for news in result]"""
    try:
        format_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    result = search_news({"timestamp": format_date})

    return [(news["title"], news["url"]) for news in result]


# Requisito 9
def search_by_category(category):
    result = search_news({"category": {"$regex": category, "$options": "i"}})
    return [(news["title"], news["url"]) for news in result]
