import logging
from typing import Union

import requests
from bs4 import BeautifulSoup
from requests import RequestException, Response

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class WebCrawlerSync:
    """Cинхронный веб-краулер"""

    def __init__(self, list_url: list):
        self.__list_url = list_url

    def __load_url(self, url: str) -> Union[Response, RequestException]:
        try:
            logger.info("Смнхронная загрузка html запушщена")
            response = requests.get(url, timeout=5)
            logger.info("Смнхронная загрузка html завершена")
        except requests.exceptions.InvalidURL as error:
            logger.error(error)
            return error
        except requests.exceptions.Timeout as error:
            logger.error(error)
            return error
        except requests.exceptions.HTTPError as error:
            logger.error(error)
            return error
        except requests.exceptions.ConnectionError as error:
            logger.error(error)
            return error

        return response

    def get_element(self, element: str) -> dict:
        url_dict = {}
        for url in self.__list_url:
            html = self.__load_url(url)
            if isinstance(html, RequestException):
                url_dict[url] = f"Вовремя загрузки произошла ошибка: {html}"
            else:
                tag = BeautifulSoup(html.text, 'lxml')
                url_dict[url] = tag.find(element).text

        return url_dict
