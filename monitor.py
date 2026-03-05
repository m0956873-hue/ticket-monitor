import requests
from playwright.sync_api import sync_playwright

URL = "https://tickets.interpark.com/onestop/schedule"

WEBHOOK = "https://discord.com/api/webhooks/1479076004927508511/qADXs4qBGVQmzIEfKQ9QZazSZ8myEVH0MGsWFum0SNuwYkXUOjCB3dVI6B-FR55DnWIQ"

def send_discord(msg):
    requests.post(WEBHOOK, json={"content": msg})

def check_ticket():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(URL)

        page.wait_for_timeout(5000)

        content = page.content()

        if "예매" in content:
            send_discord("🎫 Interpark可能有新票\n" + URL)

        browser.close()

check_ticket()
