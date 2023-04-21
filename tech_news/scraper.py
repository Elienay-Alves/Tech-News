import time
import requests


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
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
