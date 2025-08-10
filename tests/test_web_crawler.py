from src.crawler.web_crawler_async import WebcrawlerAsync
from src.crawler.web_crawler_sync import WebCrawlerSync

list_url  = ['https://pikabu.ru/', 'https://pikau.ru/']


def test_get_element():
    w = WebCrawlerSync(list_url)
    result = w.get_element('title')

    assert type(result) == dict
    assert 'Вовремя загрузки произошла ошибка' in result['https://pikau.ru/']
    assert 'Горячее' in result['https://pikabu.ru/']



async def test_get_element_async():
    w = WebcrawlerAsync(list_url)
    result = await w.get_element_async('title')
    assert type(result) == dict
    assert 'Вовремя загрузки произошла ошибка' in result['https://pikau.ru/']
    assert 'Горячее' in result['https://pikabu.ru/']