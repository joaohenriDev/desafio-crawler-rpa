import csv
import json
import logging
from pathlib import Path

from src.config import Config


class FileExporter:
    """Responsável por exportar dados para arquivos."""

    @classmethod
    def _ensure_directory_exists(cls, filepath: str) -> None:
        """Cria o diretório do arquivo caso não exista."""

        Path(filepath).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    @classmethod
    def save_to_json(
        cls,
        data: list[dict],
        filepath: str = Config.JSON_OUTPUT_PATH,
    ) -> None:
        """Salva os dados em JSON."""

        if not data:
            logging.warning(
                "Nenhum dado para salvar em JSON."
            )
            return

        try:
            cls._ensure_directory_exists(filepath)

            with open(
                filepath,
                mode="w",
                encoding="utf-8",
            ) as file:
                json.dump(
                    data,
                    file,
                    indent=4,
                    ensure_ascii=False,
                )

            logging.info(
                "Arquivo JSON salvo: %s",
                filepath,
            )

        except Exception as error:
            logging.error(
                "Erro ao salvar JSON: %s",
                error,
            )
            raise

    @classmethod
    def save_to_csv(
        cls,
        data: list[dict],
        filepath: str = Config.CSV_OUTPUT_PATH,
    ) -> None:
        """Salva os dados em CSV."""

        if not data:
            logging.warning(
                "Nenhum dado para salvar em CSV."
            )
            return

        try:
            cls._ensure_directory_exists(filepath)

            headers = data[0].keys()

            with open(
                filepath,
                mode="w",
                newline="",
                encoding="utf-8",
            ) as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=headers,
                )

                writer.writeheader()
                writer.writerows(data)

            logging.info(
                "Arquivo CSV salvo: %s",
                filepath,
            )

        except Exception as error:
            logging.error(
                "Erro ao salvar CSV: %s",
                error,
            )
            raise