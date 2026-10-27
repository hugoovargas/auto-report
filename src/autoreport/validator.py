import pandas as pd

COLUNAS_OBRIGATORIAS = [
    "id_venda",
    "data",
    "produto",
    "quantidade",
    "preco_unitario",
    "categoria",
]

def validar_vendas(vendas: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Separa as vendas válidas das inválidas e registra os motivos de rejeição."""
    colunas_ausentes = [
        coluna for coluna in COLUNAS_OBRIGATORIAS
        if coluna not in vendas.columns
    ]

    if colunas_ausentes:
        raise ValueError(f"Colunas obrigatórias ausentes: {colunas_ausentes}")

    dados = vendas.copy().reset_index(drop=True)

    # Converte temporariamente os campos para validar seus valores.
    datas = pd.to_datetime(dados["data"], errors="coerce")
    quantidades = pd.to_numeric(dados["quantidade"], errors="coerce")
    precos = pd.to_numeric(dados["preco_unitario"], errors="coerce")

    # Cada posição armazena todos os problemas encontrados na respectiva linha.
    motivos = [[] for _ in range(len(dados))]

    def registrar_problema(condicao: pd.Series, mensagem: str) -> None:
        for posicao, invalido in enumerate(condicao.fillna(True).tolist()):
            if invalido:
                motivos[posicao].append(mensagem)

    # Verifica campos obrigatórios vazios.
    for coluna in ["id_venda", "produto", "categoria", "data"]:
        vazio = (
            dados[coluna].isna()
            | dados[coluna].astype("string").str.strip().eq("")
        ).fillna(True)
        registrar_problema(vazio, f"Campo obrigatório vazio: {coluna}")

    # Verifica IDs duplicados. Compara IDs depois de remover espaços externos.
    ids = dados["id_venda"].astype("string").str.strip()
    ids_preenchidos = ids.notna() & ids.ne("")
    ids_duplicados = ids_preenchidos & ids.duplicated(keep=False)
    registrar_problema(ids_duplicados, "ID de venda duplicado")

    # Verifica datas inválidas.
    datas_invalidas = datas.isna()
    registrar_problema(datas_invalidas, "Data inválida")

    # Verifica quantidade: numérica, maior que zero e inteira.
    registrar_problema(
        quantidades.isna() | (quantidades <= 0),
        "Quantidade deve ser um número maior que zero",
    )
    registrar_problema(
        quantidades.notna() & (quantidades % 1 != 0),
        "Quantidade deve ser um número inteiro",
    )

    # Verifica preço: numérico e não negativo.
    registrar_problema(
        precos.isna() | (precos <= 0),
        "Preço unitário deve ser um número maior que zero",
    )

    possui_problema = pd.Series(
        [bool(lista) for lista in motivos],
        index=dados.index,
    )

    validas = dados.loc[~possui_problema].copy()
    invalidas = dados.loc[possui_problema].copy()

    # Normaliza os tipos dos registros válidos para facilitar os cálculos.
    validas["data"] = datas.loc[~possui_problema]
    validas["quantidade"] = quantidades.loc[~possui_problema].astype(int)
    validas["preco_unitario"] = precos.loc[~possui_problema].astype(float)

    invalidas["motivo_validacao"] = [
        "; ".join(motivos[posicao]) for posicao in invalidas.index
    ]

    return validas, invalidas
