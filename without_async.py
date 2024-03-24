from bs4 import BeautifulSoup
import requests
import datetime

def get_weather(page_dict_info):
    resp = requests.get(page_dict_info['url'])
    soup = BeautifulSoup(resp.text, 'lxml')
    weather = soup.find(class_=page_dict_info['class'])
    print(f'{page_dict_info['name']}|{weather.text} \n')



def main():

    urls = [
        {
            'name': 'Mail',
            'url': 'https://pogoda.mail.ru/prognoz/novosibirsk/',
            'class': 'information__content__temperature'
        },
        {
            'name': 'Rambler',
            'url': 'https://weather.rambler.ru/v-novosibirske/today/',
            'class': 'Njqa',
        },
        {
            'name': 'Ngs',
            'url': 'https://pogoda.ngs.ru/?from=pogoda',
            'class': 'value__main'
        }
            ]
    print('WITHOUT ASYNCIO')
    print(datetime.datetime.now())
    for page in urls:
        get_weather(page)
    print(datetime.datetime.now())  


main()