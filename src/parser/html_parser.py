import logging
import re

from bs4 import BeautifulSoup


class HtmlParser:
    """Responsável por extrair dados do HTML."""

    RATING_MAP = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }

    @classmethod
    def parse_books_list(cls, html_content: str) -> list[dict]:
        """Extrai os dados dos livros da página."""

        if not html_content:
            return []

        soup = BeautifulSoup(html_content, "html.parser")
        books = []

        book_pods = soup.select("article.product_pod")

        logging.info(
            "Encontrados %s livros.",
            len(book_pods),
        )

        for pod in book_pods:
            try:
                title_element = pod.select_one("h3 a")
                price_element = pod.select_one("p.price_color")
                availability_element = pod.select_one(
                    "p.instock.availability"
                )
                rating_element = pod.select_one(
                    "p.star-rating"
                )

                title = (
                    title_element.get(
                        "title",
                        "Desconhecido",
                    )
                    if title_element
                    else "Desconhecido"
                )

                price_text = (
                    price_element.text
                    if price_element
                    else "0.0"
                )

                price_match = re.search(
                    r"\d+\.\d+",
                    price_text,
                )

                price = (
                    float(price_match.group())
                    if price_match
                    else 0.0
                )

                in_stock = (
                    "In stock"
                    in availability_element.text
                    if availability_element
                    else False
                )

                rating = 0

                if rating_element:
                    classes = rating_element.get(
                        "class",
                        [],
                    )

                    rating = next(
                        (
                            cls.RATING_MAP[class_name]
                            for class_name in classes
                            if class_name
                            in cls.RATING_MAP
                        ),
                        0,
                    )

                books.append(
                    {
                        "title": title,
                        "price_gbp": price,
                        "in_stock": in_stock,
                        "rating": rating,
                    }
                )

            except Exception as error:
                logging.error(
                    "Erro ao processar livro: %s",
                    error,
                )

        return books