import pytest

from src.parser.html_parser import HtmlParser


@pytest.fixture
def valid_html_mock() -> str:
    """Mock de HTML válido."""

    return """
    <article class="product_pod">
        <div class="image_container">
            <a href="item.html">
                <img
                    src="thumb.jpg"
                    alt="Livro de Teste"
                    class="thumbnail"
                >
            </a>
        </div>

        <p class="star-rating Three"></p>

        <h3>
            <a
                href="item.html"
                title="O Guia Perfeito de Python Extenso"
            >
                O Guia Perfeito...
            </a>
        </h3>

        <div class="product_price">
            <p class="price_color">Â£42.50</p>

            <p class="instock availability">
                <i class="icon-ok"></i>
                In stock
            </p>
        </div>
    </article>
    """


def test_parse_books_list_success(
    valid_html_mock: str,
) -> None:
    """Valida extração completa dos dados."""

    result = HtmlParser.parse_books_list(
        valid_html_mock
    )

    assert len(result) == 1

    book = result[0]

    assert (
        book["title"]
        == "O Guia Perfeito de Python Extenso"
    )

    assert book["price_gbp"] == 42.50
    assert book["in_stock"] is True
    assert book["rating"] == 3


def test_parse_books_list_empty_html() -> None:
    """Valida retorno vazio para HTML vazio."""

    result = HtmlParser.parse_books_list("")

    assert result == []


def test_parse_books_list_invalid_html() -> None:
    """Valida comportamento defensivo."""

    invalid_html = """
    <article class="product_pod">
        <h3>Sem dados</h3>
    </article>
    """

    result = HtmlParser.parse_books_list(
        invalid_html
    )

    assert len(result) == 1

    book = result[0]

    assert book["title"] == "Desconhecido"
    assert book["price_gbp"] == 0.0
    assert book["in_stock"] is False
    assert book["rating"] == 0