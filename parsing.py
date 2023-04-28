import requests
from bs4 import BeautifulSoup


def anonse():
    list_card_url = []

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36'
    }
    anonse_list = []
    for page in range(1, 4):
        s = 0
        url = f'https://www.playground.ru/news/announces?p={page}'
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        data = soup.find_all('div', class_="post-content")
        anonse_name = []
        for i in data:
            anonse = i.find('div', class_="post-title")
            text = anonse.find('a').text
            anonse_name.append(text)
        data = soup.find_all('div', class_="post-content")
        for i in data:
            anonse = i.find('div', class_="post-metadata")
            inf = anonse.find('div')
            anonse_time = inf.find('time').text
            anonse_list.append(anonse_time + '  ' + anonse_name[s])
            s += 1

    f = open('anonse.txt', 'w')
    for i in anonse_list:
        f.write(i + '\n')


def release():
    list_card_url = []

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36'
    }

    release_list = []
    for page in range(1, 4):
        s = 0
        url = f'https://www.playground.ru/news/releases?p={page}'
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        data = soup.find_all('div', class_="post-content")
        release_name = []
        for i in data:
            release = i.find('div', class_="post-title")
            text = release.find('a').text
            release_name.append(text)
        data = soup.find_all('div', class_="post-content")
        for i in data:
            release = i.find('div', class_="post-metadata")
            inf = release.find('div')
            release_time = inf.find('time').text
            release_list.append(release_time + '  ' + release_name[s])
            s += 1

    f = open('release.txt', 'w')
    for i in release_list:
        f.write(i + '\n')


def freebies():
    list_card_url = []

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36'
    }
    freebies_list = []
    for page in range(1, 4):
        s = 0
        url = f'https://www.playground.ru/news/freebies?p={page}'
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        data = soup.find_all('div', class_="post-content")
        freebies_name = []
        for i in data:
            freebies = i.find('div', class_="post-title")
            text = freebies.find('a').text
            freebies_name.append(text)
        data = soup.find_all('div', class_="post-content")
        for i in data:
            freebies = i.find('div', class_="post-metadata")
            inf = freebies.find('div')
            freebies_time = inf.find('time').text
            freebies_list.append(freebies_time + '  ' + freebies_name[s])
            s += 1

    f = open('freebies.txt', 'w')
    for i in freebies_list:
        f.write(i + '\n')
