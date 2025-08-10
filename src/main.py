import asyncio
import time

from src.crawler.web_crawler_async import WebcrawlerAsync
from src.crawler.web_crawler_sync import WebCrawlerSync


async def async_main():
    w = WebcrawlerAsync(['https://pikabu.ru/', 'https://pikau.ru/', 'https://solvit.space/', 'https://www.rbc.ru/',
                         'https://www.vesti.ru/'])

    res = await w.get_element_async('title')
    print(res)


def sync_main():
    w = WebCrawlerSync(['https://pikabu.ru/', 'https://pikau.ru/', 'https://solvit.space/', 'https://www.rbc.ru/',
                        'https://www.vesti.ru/'])
    res = w.get_element('title')
    print(res)


start = time.time()
asyncio.run(async_main())
print(f"Время асинхронной загрузки: {str(time.time() - start)}")

start = time.time()
sync_main()
print(f"Время синхронной загрузки: {str(time.time() - start)}")
