import logging

import requests

from src.config import Config
from src.crawler.base_scraper import BaseScraper


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class StaticHtmlScraper(BaseScraper):
    """Scraper para páginas estáticas usando Requests."""

    def __init__(self):
        self.session = requests.Session()

    def fetch_page_html(self, url: str) -> str:
        """Faz o download do HTML da página."""

        retries = 3

        for attempt in range(1, retries + 1):
            try:
                Config.wait_delay()

                logging.info(
                    "Requisição para %s (%s/%s)",
                    url,
                    attempt,
                    retries,
                )

                response = self.session.get(
                    url,
                    headers=Config.get_headers(),
                    timeout=10,
                )

                response.raise_for_status()

                return response.text

            except requests.RequestException as error:
                logging.warning(
                    "Falha na requisição %s: %s",
                    url,
                    error,
                )

                if attempt == retries:
                    logging.error(
                        "Número máximo de tentativas excedido: %s",
                        url,
                    )
                    raise