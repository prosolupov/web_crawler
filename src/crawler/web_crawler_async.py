import logging
from typing import Union

import aiohttp
from bs4 import BeautifulSoup

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class WebcrawlerAsync:
    """Асинхронный веб-краулер"""

    def __init__(self, list_url: list):
        self.__list_url = list_url

    async def __load_url(self, url: str) -> Union[str, aiohttp.ClientError]:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, timeout=5) as response:
                    logger.info("Асинхронная загрузка html запущена")
                    response = await response.text()
                    logger.info("Асинхронная загрузка html завершена")
            except aiohttp.InvalidURL as error:
                logger.error(error)
                return error
            except aiohttp.ServerTimeoutError as error:
                logger.error(error)
                return error
            except aiohttp.ClientResponseError as error:
                logger.error(error)
                return error
            except aiohttp.ClientOSError as error:
                logger.error(error)
                return error

        return response

    async def get_element_async(self, element: str) -> dict:
        url_dict = {}
        for url in self.__list_url:
            html = await self.__load_url(url)
            if isinstance(html, aiohttp.ClientError):
                url_dict[url] = f"Вовремя загрузки произошла ошибка: {html}"
            else:
                tag = BeautifulSoup(html, 'lxml')
                url_dict[url] = tag.find(element).text

        return url_dict
