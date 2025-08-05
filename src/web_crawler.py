import asyncio
import aiohttp
import requests
import time
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class WebCrawler:
    """Асинхронный веб-краулер"""