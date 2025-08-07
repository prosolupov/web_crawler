import logging

import aiohttp

from src.crawler.webcrawler_base import WebcrawlerBase

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class WebcrawlerAsync(WebcrawlerBase):
    """Асинхронный веб-краулер"""
    async def load_url(self):
        ...