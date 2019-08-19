from flask import Flask, escape, request
from bs4 import BeautifulSoup
import requests
from Player import Player


source = requests.get('https://sofifa.com/?hl=en-US').text

soup = BeautifulSoup(source, 'html.parser')

#print(soup.prettify())

# table = soup.find('tbody')
# name = table.tr.div.text
# print(name)

# country = soup.find('div', class_='bp3-text-overflow-ellipsis').a['title']
# print(country)


def names_list():
    # return [i for i in soup.find_all('a', class_='nowrap')]
    l = []
    for i in soup.find_all('a', class_='nowrap'):
        name = i.text
        l.append(name)
    return l


def countries_list():
    l = []
    for i in soup.find_all('div', class_='bp3-text-overflow-ellipsis'):
        c = i.a

        if c.get('rel') == ['nofollow']:
            l.append(c.get('title'))

        # country = str(c)
        # if len(country) > 100:
        #     country = country.split('="')[3]
        #     country = country.split('">')[0]
        #     l.append(country)
    return l


def ovr_list():
    l = []
    for i in soup.find_all('td', class_='col col-oa'):
        ovr = i.span.text
        l.append(ovr)
    return l


def pot_list():
    l = []
    for i in soup.find_all('td', class_='col col-pt'):
        pot = i.span.text
        l.append(pot)
    return l


names = names_list()
countries = countries_list()
ovrs = ovr_list()
pots = pot_list()

players = []
for i in range(0, len(names)):
    p = Player(names[i], countries[i], ovrs[i], pots[i])
    players.append(p.__str__())

print("\n".join(players))
