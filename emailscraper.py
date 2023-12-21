from collections import deque
import re
from bs4 import BeautifulSoup
import requests
import urllib.parse

def get_base_url(url):
    parts = urllib.parse.urlsplit(url)
    return f'{parts.scheme}://{parts.netloc}'

def process_url(url):
    parts = urllib.parse.urlsplit(url)
    base_url = get_base_url(url)
    path = url[:url.rfind('/')+1] if '/' in parts.path else url

    try:
        response = requests.get(url)
        response.raise_for_status()
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.HTTPError):
        return set(), set()

    new_emails = set(re.findall(r'[a-z0-9.\-+_]+@\w+\.[a-z.]+', response.text, re.I))
    soup = BeautifulSoup(response.text, 'html.parser')

    new_urls = set()
    for anchor in soup.find_all('a'):
        link = anchor.get('href', '')
        if link.startswith('/'):
            link = base_url + link
        elif not link.startswith(('http', 'https')):
            link = urllib.parse.urljoin(path, link)

        new_urls.add(link)

    return new_emails, new_urls

def main():
    user_url = input('[+] Masukan url: ')
    urls = deque([user_url])
    scraped_urls = set()
    emails = set()
    count = 0
    limit = int(input('[+] Masukan limit pencarian: '))

    try:
        while urls and count < limit:
            count += 1
            url = urls.popleft()

            if url in scraped_urls:
                continue

            print(f'{count} Memproses {url}')

            new_emails, new_urls = process_url(url)
            emails.update(new_emails)
            urls.extend(new_url for new_url in new_urls if new_url not in urls and new_url not in scraped_urls)
            scraped_urls.add(url)

    except KeyboardInterrupt:
        print('[-] Closing!')

    print('\nProses Selesai!')
    print(f'\n{len(emails)} email ditemukan \n =======================================')

    for mail in emails:
        print('  ' + mail)

if __name__ == "__main__":
    main()

