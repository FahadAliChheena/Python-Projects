import requests
from bs4 import BeautifulSoup
import sys
import re

def extract_emails_from_text(text):
    email_regex = r"[\w\.-]+@[\w\.-]+"
    emails = re.findall(email_regex, text)
    return emails

def main():
    if len(sys.argv) < 2:
        print("Usage: python email_scraper.py [url]")
        return

    link = sys.argv[1]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    }

    response = requests.get(link, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch the webpage.")
        return

    page_content = response.text
    soup = BeautifulSoup(page_content, "html.parser")

    emails = set()

    # Search for emails using regex
    emails.update(extract_emails_from_text(page_content))

    print("Extracted email addresses:")
    for email in emails:
        print(email)

if __name__ == "__main__":
    main()