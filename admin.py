from selenium import webdriver
import urllib
import os

WORDLE = "SEGFAULT"
PORT = int(os.getenv("APP_PORT", "8000"))


def _get_url(url, cookie=None):
    if cookie is None:
        cookie = {"name": "name", "value": "value"}

    cookie.update({"domain": "127.0.0.1"})

    options = webdriver.ChromeOptions()
    for _ in [
        "headless",
        "window-size=1920x1080",
        "disable-gpu",
        "no-sandbox",
        "disable-dev-shm-usage",
    ]:
        options.add_argument(_)

    driver = webdriver.Chrome("chromedriver", options=options)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.get(f"http://127.0.0.1:{PORT}/")
    driver.add_cookie(cookie)
    print(url)
    driver.get(url)
    driver.quit()

    return True


def checks_client_page(word: str):
    cookie = {"name": "WORDLE", "value": WORDLE}
    url = f"http://127.0.0.1:{PORT}/?word={urllib.parse.quote(word)}"

    _get_url(url, cookie)

    return WORDLE == word.upper()
