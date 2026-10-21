from pathlib import Path

import pandas as pd

def ler_vendas(caminho: Path) -> pd.DataFrame:
    if not caminho.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {caminho}"
        )

    return pd.read_csv(caminho)
