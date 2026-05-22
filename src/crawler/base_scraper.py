from abc import ABC, abstractmethod


class BaseScraper(ABC):
    """Contrato base para todos os scrapers do projeto."""

    @abstractmethod
    def fetch_page_html(self, url: str) -> str:
        """Retorna o HTML bruto da página."""