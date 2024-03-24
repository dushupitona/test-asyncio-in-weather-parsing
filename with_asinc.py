import asyncio
from bs4 import BeautifulSoup
from aiohttp_requests import requests
import datetime


async def get_weather(page_dict_info):
    resp = await requests.get(page_dict_info['url'])
    soup = BeautifulSoup(await resp.text(), 'lxml')
    weather = soup.find(class_=page_dict_info['class'])
    print(f'{page_dict_info['name']}|{weather.text} \n')



async def main():

    tasks = []

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
    
    for page in urls:
        task = asyncio.create_task(get_weather(page))
        tasks.append(task)
        
    await asyncio.gather(*tasks)
    

print('WITH ASYNCIO')
print(datetime.datetime.now())
asyncio.run(main())
print(datetime.datetime.now())




