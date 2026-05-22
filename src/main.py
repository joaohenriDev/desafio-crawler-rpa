import logging
import sys

from src.config import Config
from src.crawler.static_html import StaticHtmlScraper
from src.parser.html_parser import HtmlParser
from src.storage.file_exporter import FileExporter


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


def run_scraper() -> None:
    """Executa o fluxo principal do scraper."""

    logging.info("Iniciando scraper...")

    try:
        scraper = StaticHtmlScraper()

        html_content = scraper.fetch_page_html(
            Config.BASE_URL
        )

        if not html_content:
            logging.error(
                "HTML vazio retornado pelo scraper."
            )
            return

        books = HtmlParser.parse_books_list(
            html_content
        )

        if not books:
            logging.warning(
                "Nenhum livro encontrado."
            )
            return

        logging.info(
            "%s livros extraídos com sucesso.",
            len(books),
        )

        FileExporter.save_to_json(books)
        FileExporter.save_to_csv(books)

        logging.info(
            "Processo finalizado com sucesso."
        )

    except Exception as error:
        logging.critical(
            "Erro crítico na execução: %s",
            error,
        )
        sys.exit(1)


if __name__ == "__main__":
    run_scraper()