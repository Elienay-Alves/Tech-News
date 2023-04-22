import time
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url=None):
    if url is None:
        return None

    time.sleep(1)
    try:
        result = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        result.raise_for_status()
        return result.text
    except requests.exceptions.RequestException as err:
        print(f"Erro ao obter a página {url}: {err}")
        return None


# Requisito 2
def scrape_updates(html_content):
    try:
        selector_obj = Selector(text=html_content)
        links = selector_obj.css(".entry-title > a::attr(href)").getall()
    except Exception as err:
        print(f"Erro ao analisar HTML: {err}")
        links = []

    if not links:
        print(f"Nenhum link encontrado com o seletor '{Selector}")

    return links


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        selector_obj = Selector(text=html_content)
        next_link = selector_obj.css("a.next::attr(href)").get()
    except Exception as err:
        print(f"Erro ao analisar HTML: {err}")
        next_link = None

    if next_link is None:
        print("Nenhum link encontrado com o seletor")

    return next_link


# Requisito 4
def scrape_news(html_content):
    try:
        selector_obj = Selector(text=html_content)
        url = selector_obj.css("link[rel='canonical']::attr(href)").get()
        title = (
            selector_obj.css(
                "div.entry-header-inner h1.entry-title::text"
            ).get().strip()
        )

        timestamp = selector_obj.css("li.meta-date::text").get()
        writer = selector_obj.css("span.author a::text").get()
        reading_time = selector_obj.css(
            "li.meta-reading-time::text"
        ).get().split()[0]
        time = int("".join(filter(str.isdigit, reading_time)))
        summary = selector_obj.css(
            "div.entry-content > p:first-of-type *::text"
        ).getall()
        summary = "".join(summary).strip()
        category = selector_obj.css(
            "div.meta-category a span.label::text"
        ).get()

    except Exception as err:
        print(f"Erro ao analisar HTML: {err}")
        return None

    if not all([url, title, timestamp, writer, time, summary, category]):
        print("Algumas informações não foram encontradas")
        return None

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    page = fetch("https://blog.betrybe.com/")
    links = scrape_updates(page)

    while len(links) < amount:
        next_page = scrape_next_page_link(page)
        page = fetch(next_page)
        news_links = scrape_updates(page)
        for news_link in news_links:
            links.append(news_link)

    news_list = []

    for index in range(amount):
        req = fetch(links[index])
        news_list.append(scrape_news(req))

    create_news(news_list)

    return news_list
