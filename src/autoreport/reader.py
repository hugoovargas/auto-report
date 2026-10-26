from pathlib import Path

import pandas as pd

def ler_vendas(caminho: Path) -> pd.DataFrame:
    """Lê um arquivo CSV de vendas e retorna seus dados em um DataFrame."""
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    if not caminho.is_file():
        raise ValueError(f"O caminho informado não é um arquivo: {caminho}")

    try:
        return pd.read_csv(caminho)
    except pd.errors.EmptyDataError as erro:
        raise ValueError(f"O arquivo CSV está vazio: {caminho}") from erro
    except pd.errors.ParserError as erro:
        raise ValueError(f"Não foi possível interpretar o CSV: {caminho}") from erro
