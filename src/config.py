import os
import random
import time


class Config:
    BASE_URL = "http://books.toscrape.com/"

    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ...",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ...",
        "Mozilla/5.0 (X11; Linux x86_64) ..."
    ]

    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
    OUTPUT_DIR = os.path.join(ROOT_DIR, "output")

    JSON_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "books_data.json")
    CSV_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "books_data.csv")

    @classmethod
    def get_headers(cls) -> dict:
        """Retorna headers HTTP para as requisições."""

        return {
            "User-Agent": random.choice(cls.USER_AGENTS),
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": (
                "text/html,application/xhtml+xml,"
                "application/xml;q=0.9,image/avif,image/webp"
            ),
        }

    @classmethod
    def wait_delay(cls) -> None:
        """Aplica atraso aleatório entre requisições."""

        time.sleep(random.uniform(1.0, 3.0))