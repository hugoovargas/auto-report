import pandas as pd

COLUNAS_OBRIGATORIAS = [
    "id_venda",
    "data",
    "produto",
    "quantidade",
    "preco_unitario",
    "categoria",
]

def validar_vendas(vendas: pd.DataFrame,) -> tuple[pd.DataFrame, pd.DataFrame]:

    colunas_ausentes = [
        coluna
        for coluna in COLUNAS_OBRIGATORIAS
        if coluna not in vendas.columns
    ]

    if colunas_ausentes:
        raise ValueError(
            f"Colunas obrigatórias ausentes: {colunas_ausentes}"
        )

    dados = vendas.copy().reset_index(drop=True)

    # Prepara os dados para validar datas e números.
    datas = pd.to_datetime(dados["data"], errors="coerce")

    quantidades = pd.to_numeric(dados["quantidade"], errors="coerce")

    precos = pd.to_numeric(dados["preco_unitario"], errors="coerce")

    # Cada posição armazena os problemas encontrados naquela linha.
    motivos = [[] for _ in range(len(dados))]

    def registrar_problema(condicao: pd.Series, mensagem: str,) -> None:
        for posicao, invalido in enumerate(condicao.tolist()):
            if invalido:
                motivos[posicao].append(mensagem)

    # Verifica campos obrigatórios vazios.
    for coluna in ["id_venda", "produto", "categoria", "data"]:
        vazio = (
            dados[coluna].isna()
            | dados[coluna].astype("string").str.strip().eq("")
        ).fillna(True)

        registrar_problema(
            vazio,
            f"Campo obrigatório vazio: {coluna}",
        )

    # Verifica identificadores duplicados.
    ids_preenchidos = (
        dados["id_venda"].notna()
        & dados["id_venda"].astype("string").str.strip().ne("")
    )

    ids_duplicados = (
        ids_preenchidos
        & dados["id_venda"].duplicated(keep=False)
    )

    registrar_problema(
        ids_duplicados,
        "ID de venda duplicado",
    )

    # Verifica datas inválidas.
    registrar_problema(
        datas.isna(),
        "Data inválida",
    )

    # Verifica quantidades.
    registrar_problema(
        quantidades.isna() | (quantidades <= 0),
        "Quantidade deve ser um número maior que zero",
    )

    registrar_problema(
        quantidades.notna() & (quantidades % 1 != 0),
        "Quantidade deve ser um número inteiro",
    )

    # Verifica preços.
    registrar_problema(
        precos.isna() | (precos < 0),
        "Preço unitário deve ser um número maior ou igual a zero",
    )

    # Separa os registros sem problemas dos registros inválidos.
    possui_problema = pd.Series(
        [bool(lista) for lista in motivos],
        index=dados.index,
    )

    validas = dados.loc[~possui_problema].copy()
    invalidas = dados.loc[possui_problema].copy()

    # Converte os campos numéricos e a data dos registros válidos.
    validas["data"] = datas.loc[~possui_problema]
    validas["quantidade"] = quantidades.loc[~possui_problema].astype(int)
    validas["preco_unitario"] = precos.loc[~possui_problema]

    # Preserva os registros inválidos e explica seus problemas.
    invalidas["motivo_validacao"] = [
        "; ".join(motivos[posicao])
        for posicao in invalidas.index
    ]

    return validas, invalidas
