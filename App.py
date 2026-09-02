import streamlit as st
import pandas as pd
import plotly.express as px


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)


# =========================================================
# CARREGAMENTO DOS DADOS
# =========================================================

@st.cache_data
def carregar_dados():
    """
    Carrega o dataset local do projeto.

    O uso de cache evita que o CSV seja relido
    a cada interação com os filtros do Streamlit.
    """
    return pd.read_csv("dados-imersao-final.csv")


df = carregar_dados()


# =========================================================
# BARRA LATERAL — FILTROS
# =========================================================

st.sidebar.header("🔍 Filtros")


# Filtro de Ano
anos_disponiveis = sorted(df["ano"].dropna().unique())

anos_selecionados = st.sidebar.multiselect(
    "Ano",
    anos_disponiveis,
    default=anos_disponiveis,
)


# Filtro de Senioridade
senioridades_disponiveis = sorted(df["senioridade"].dropna().unique())

senioridades_selecionadas = st.sidebar.multiselect(
    "Senioridade",
    senioridades_disponiveis,
    default=senioridades_disponiveis,
)


# Filtro por Tipo de Contrato
contratos_disponiveis = sorted(df["contrato"].dropna().unique())

contratos_selecionados = st.sidebar.multiselect(
    "Tipo de Contrato",
    contratos_disponiveis,
    default=contratos_disponiveis,
)


# Filtro por Tamanho da Empresa
tamanhos_disponiveis = sorted(df["tamanho_empresa"].dropna().unique())

tamanhos_selecionados = st.sidebar.multiselect(
    "Tamanho da Empresa",
    tamanhos_disponiveis,
    default=tamanhos_disponiveis,
)


# =========================================================
# FILTRAGEM DO DATAFRAME
# =========================================================

df_filtrado = df[
    (df["ano"].isin(anos_selecionados))
    & (df["senioridade"].isin(senioridades_selecionadas))
    & (df["contrato"].isin(contratos_selecionados))
    & (df["tamanho_empresa"].isin(tamanhos_selecionados))
]


# =========================================================
# CONTEÚDO PRINCIPAL
# =========================================================

st.title("🎲 Dashboard de Análise de Salários na Área de Dados")

st.markdown(
    """
    Explore os dados salariais na área de dados nos últimos anos.
    Utilize os filtros à esquerda para refinar sua análise.
    """
)


# =========================================================
# MÉTRICAS PRINCIPAIS — KPIs
# =========================================================

st.subheader("Métricas gerais (Salário anual em USD)")


if not df_filtrado.empty:

    salario_medio = df_filtrado["usd"].mean()

    salario_maximo = df_filtrado["usd"].max()

    total_registros = df_filtrado.shape[0]

    modo_cargo = df_filtrado["cargo"].mode()

    cargo_mais_frequente = (
        modo_cargo.iloc[0]
        if not modo_cargo.empty
        else "N/A"
    )

else:

    salario_medio = 0

    salario_maximo = 0

    total_registros = 0

    cargo_mais_frequente = "N/A"


col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Salário médio",
    f"${salario_medio:,.0f}",
)


col2.metric(
    "Salário máximo",
    f"${salario_maximo:,.0f}",
)


col3.metric(
    "Total de registros",
    f"{total_registros:,}",
)


col4.metric(
    "Cargo mais frequente",
    cargo_mais_frequente,
)


st.markdown("---")


# =========================================================
# ANÁLISES VISUAIS
# =========================================================

st.subheader("Gráficos")


# ---------------------------------------------------------
# LINHA 1 DE GRÁFICOS
# ---------------------------------------------------------

col_graf1, col_graf2 = st.columns(2)


# =========================================================
# TOP 10 CARGOS POR SALÁRIO MÉDIO
# =========================================================

with col_graf1:

    if not df_filtrado.empty:

        top_cargos = (
            df_filtrado
            .groupby("cargo", as_index=False)["usd"]
            .mean()
            .nlargest(10, "usd")
            .sort_values("usd", ascending=True)
        )

        grafico_cargos = px.bar(
            top_cargos,
            x="usd",
            y="cargo",
            orientation="h",
            title="Top 10 cargos por salário médio",
            labels={
                "usd": "Média salarial anual (USD)",
                "cargo": "",
            },
        )

        grafico_cargos.update_layout(
            title_x=0.1,
            yaxis={
                "categoryorder": "total ascending"
            },
        )

        st.plotly_chart(
            grafico_cargos,
            use_container_width=True,
        )

    else:

        st.warning(
            "Nenhum dado para exibir no gráfico de cargos."
        )


# =========================================================
# DISTRIBUIÇÃO DOS SALÁRIOS
# =========================================================

with col_graf2:

    if not df_filtrado.empty:

        grafico_hist = px.histogram(
            df_filtrado,
            x="usd",
            nbins=30,
            title="Distribuição de salários anuais",
            labels={
                "usd": "Faixa salarial (USD)",
                "count": "",
            },
        )

        grafico_hist.update_layout(
            title_x=0.1
        )

        st.plotly_chart(
            grafico_hist,
            use_container_width=True,
        )

    else:

        st.warning(
            "Nenhum dado para exibir no gráfico de distribuição."
        )


# ---------------------------------------------------------
# LINHA 2 DE GRÁFICOS
# ---------------------------------------------------------

col_graf3, col_graf4 = st.columns(2)


# =========================================================
# PROPORÇÃO DE TRABALHO REMOTO
# =========================================================

with col_graf3:

    if not df_filtrado.empty:

        remoto_contagem = (
            df_filtrado["remoto"]
            .value_counts()
            .reset_index()
        )

        remoto_contagem.columns = [
            "tipo_trabalho",
            "quantidade",
        ]

        grafico_remoto = px.pie(
            remoto_contagem,
            names="tipo_trabalho",
            values="quantidade",
            title="Proporção dos tipos de trabalho",
            hole=0.5,
        )

        grafico_remoto.update_traces(
            textinfo="percent+label"
        )

        grafico_remoto.update_layout(
            title_x=0.1
        )

        st.plotly_chart(
            grafico_remoto,
            use_container_width=True,
        )

    else:

        st.warning(
            "Nenhum dado para exibir no gráfico dos tipos de trabalho."
        )


# =========================================================
# SALÁRIO MÉDIO DE DATA SCIENTIST POR PAÍS
# =========================================================

with col_graf4:

    if not df_filtrado.empty:

        df_ds = df_filtrado[
            df_filtrado["cargo"] == "Data Scientist"
        ]

        if not df_ds.empty:

            media_ds_pais = (
                df_ds
                .groupby(
                    "residencia_iso3",
                    as_index=False,
                )["usd"]
                .mean()
            )

            grafico_paises = px.choropleth(
                media_ds_pais,
                locations="residencia_iso3",
                color="usd",
                color_continuous_scale="RdYlGn",
                title="Salário médio de Cientista de Dados por país",
                labels={
                    "usd": "Salário médio (USD)",
                    "residencia_iso3": "País",
                },
            )

            grafico_paises.update_layout(
                title_x=0.1
            )

            st.plotly_chart(
                grafico_paises,
                use_container_width=True,
            )

        else:

            st.info(
                "Não há registros de Data Scientist "
                "para os filtros selecionados."
            )

    else:

        st.warning(
            "Nenhum dado para exibir no gráfico de países."
        )


# =========================================================
# TABELA DE DADOS DETALHADOS
# =========================================================

st.markdown("---")

st.subheader("Dados Detalhados")


if not df_filtrado.empty:

    st.dataframe(
        df_filtrado,
        use_container_width=True,
    )

else:

    st.info(
        "Nenhum registro encontrado com os filtros selecionados."
    )
