import requests
import time


# Requisito 1
def fetch(url):
    response = None
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        time.sleep(1)
        response.headers["Content-Type"]
    except requests.Timeout:
        return None
    finally:
        if response:
            return response.text
        else:
            None


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
