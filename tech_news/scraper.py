from bs4 import BeautifulSoup
import requests
import time
import re


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
    soup = BeautifulSoup(html_content, "html.parser")
    post = soup.find_all("a", {"class": "cs-overlay-link"})
    links = []
    for item in post:
        links.append(str(item["href"]))
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        return soup.find("a", {"class": "next page-numbers"})["href"]
    except TypeError:
        return None


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    url = soup.find("link", {"rel": "canonical"})["href"]

    title = soup.find("h1", {"class": "entry-title"}).text

    date = soup.find("li", {"class": "meta-date"}).text

    writer = soup.find("a", {"class": "url fn n"}).text

    time = soup.find("li", {"class": "meta-reading-time"}).text
    readingTime = int(re.findall(r"\d+", time)[0])

    summary = soup.find("div", {"class": "entry-content"}).p.text

    category = soup.find("span", {"class": "label"}).text

    dict_post = {
        "url": url,
        "title": title.rstrip(' ').rstrip("\xa0"),
        "timestamp": date,
        "writer": writer,
        "reading_time": readingTime,
        "summary": summary.rstrip(' ').rstrip("\xa0"),
        "category": category
    }
    return dict_post


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
