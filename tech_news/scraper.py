import time
import requests
from parsel import Selector


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
def scrape_updates(html_content, selector=".entry-title > a::attr(href)"):
    try:
        selector_obj = Selector(text=html_content)
        links = selector_obj.css(selector).getall()
    except Exception as err:
        print(f"Erro ao analisar HTML: {err}")
        links = []

    if not links:
        print(f"Nenhum link encontrado com o seletor '{Selector}")

    return links


# Requisito 3
def scrape_next_page_link(html_content, selector="a.next::attr(href)"):
    try:
        selector_obj = Selector(text=html_content)
        next_link = selector_obj.css(selector).get()
    except Exception as err:
        print(f"Erro ao analisar HTML: {err}")
        next_link = None

    if next_link is None:
        print(f"Nenhum link encontrado com o seletor '{selector}")

    return next_link


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
