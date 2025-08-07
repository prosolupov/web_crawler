class WebcrawlerBase:
    """Асинхронный веб-краулер"""

    def __init__(self, list_url: list):
        self.list_url = [url for url in list_url if url.split('.')[1] in ['ru', 'com', 'net']]
        print(self.list_url)