# 📊 Dashboard de Análise de Salários na Área de Dados

> Data App interativo desenvolvido com **Python, Pandas, Streamlit e Plotly** para explorar salários, senioridade, contratos, trabalho remoto e distribuição geográfica de profissionais da área de Dados.

![Python](https://img.shields.io/badge/Python-Data%20Analytics-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Data%20App-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly&logoColor=white)
![Data Visualization](https://img.shields.io/badge/Data-Visualization-2E8B57)
![Dashboard](https://img.shields.io/badge/Data-Interactive%20Dashboard-7952B3)
![Alura](https://img.shields.io/badge/Alura-Imersão%20Dados-0A3871)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

---

## 📌 Sobre o Projeto

Este projeto consiste em um **dashboard interativo para análise de salários na área de Dados**, desenvolvido durante a **Imersão Python com Dados II da Alura**.

A aplicação utiliza **Python, Pandas, Streamlit e Plotly** para transformar um dataset salarial em uma experiência analítica navegável pelo navegador.

O usuário pode aplicar filtros, acompanhar indicadores e explorar diferentes dimensões do mercado de trabalho em Dados.

O projeto combina:

- carregamento e preparação de dados;
- filtros interativos;
- KPIs;
- agregações com Pandas;
- visualizações com Plotly;
- mapa geográfico;
- tratamento de filtros sem resultados;
- construção de Data App com Streamlit.

---

## 🎯 Objetivo

Construir uma aplicação capaz de transformar dados tabulares em uma interface interativa para exploração e análise.

O projeto trabalha conceitos como:

- Data Analytics
- Data Visualization
- Pandas
- Streamlit
- Plotly
- DataFrames
- KPIs
- filtros
- agregações
- dashboards
- Data Apps
- UX aplicada a dados

---

## 🧠 Perguntas Analíticas

O dashboard permite explorar questões como:

- Qual é o salário médio dos profissionais de Dados?
- Qual é o maior salário presente no recorte analisado?
- Quais cargos possuem maior salário médio?
- Qual cargo aparece com maior frequência?
- Como os salários estão distribuídos?
- Qual é a proporção entre modalidades de trabalho?
- Como o salário de Data Scientists varia entre países?
- Como senioridade, contrato e tamanho da empresa alteram os resultados?

---

## 🔄 Pipeline Analítico

```text
Dataset CSV
    ↓
Carregamento
    ↓
Pandas
    ↓
Filtros
    ↓
DataFrame Filtrado
    ↓
KPIs
    ↓
Agregações
    ↓
Plotly
    ↓
Streamlit
    ↓
Dashboard Interativo
    ↓
Exploração pelo Usuário
```

---

## 🔍 Filtros Interativos

A barra lateral permite selecionar diferentes dimensões do dataset:

- Ano
- Senioridade
- Tipo de Contrato
- Tamanho da Empresa

Os filtros são aplicados simultaneamente ao DataFrame.

df_filtrado = df[
    (df["ano"].isin(anos_selecionados))
    & (df["senioridade"].isin(senioridades_selecionadas))
    & (df["contrato"].isin(contratos_selecionados))
    & (df["tamanho_empresa"].isin(tamanhos_selecionados))
]

Isso permite ao usuário alterar dinamicamente o recorte da análise.

---

## 📌 KPIs

O dashboard apresenta quatro indicadores principais:

- Salário Médio
- Salário Máximo
- Total de Registros
- Cargo Mais Frequente

Essas métricas são recalculadas de acordo com os filtros aplicados.

Caso nenhuma observação corresponda aos filtros, o sistema evita erros e apresenta valores padrão.

---

## 📊 Visualizações

1. Top 10 cargos por salário médio

Gráfico de barras horizontais com os cargos de maior média salarial.

Processo:

DataFrame Filtrado
      ↓
GroupBy por Cargo
      ↓
Média Salarial
      ↓
Top 10
      ↓
Plotly Bar Chart

2. Distribuição dos salários

Histograma com a distribuição dos salários anuais em USD.

Essa visualização permite observar:

concentração;
dispersão;
faixas salariais;
assimetrias;
valores extremos.

3. Modalidade de trabalho

Gráfico de rosca com a distribuição entre os tipos de trabalho presentes no dataset.

A análise utiliza:

value_counts()

para calcular a frequência de cada modalidade.

4. Salário médio de Data Scientist por país

Mapa coroplético que apresenta o salário médio de profissionais classificados como Data Scientist por país.

Fluxo:

DataFrame
   ↓
Filtro: Data Scientist
   ↓
GroupBy por País
   ↓
Média Salarial
   ↓
Choropleth

Caso não existam registros de Data Scientist no recorte selecionado, a aplicação apresenta uma mensagem informativa em vez de tentar gerar um gráfico vazio.

---

## 🗂️ Dados Detalhados

Além dos KPIs e gráficos, o dashboard apresenta o DataFrame filtrado.

Isso permite ao usuário observar diretamente os registros que sustentam as visualizações.

## ⚙️ Carregamento dos Dados

O projeto utiliza o dataset armazenado no próprio repositório:

dados-imersao-final.csv

O carregamento utiliza cache do Streamlit:

@st.cache_data
def carregar_dados():
    return pd.read_csv("dados-imersao-final.csv")

Isso evita leituras repetidas do arquivo durante interações com a aplicação.

---

## 🛡️ Tratamento de Edge Cases

A aplicação contempla cenários em que os filtros retornam zero registros.

Nesse caso:

Salário médio → 0
Salário máximo → 0
Total de registros → 0
Cargo mais frequente → N/A

As visualizações também são protegidas contra DataFrames vazios.

Isso evita erros durante a navegação e melhora a experiência do usuário.

---

## 🧠 Arquitetura da Aplicação

```

┌─────────────────────┐
│       CSV           │
│ Dados Salariais     │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│       Pandas        │
│ DataFrame / Filtros │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│        KPIs         │
│     Agregações      │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│       Plotly        │
│ Visualizações       │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│      Streamlit      │
│ Interface / Filtros │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│       Usuário       │
│ Exploração Analítica│
└─────────────────────┘
```

---

## 🛠️ Tecnologias

Tecnologia	Aplicação
Python	Linguagem principal
Pandas	Manipulação e análise dos dados
Streamlit	Interface e construção do Data App
Plotly	Visualizações interativas
CSV	Fonte de dados
Git	Versionamento
GitHub	Repositório e documentação

---

## 📂 Estrutura do Projeto

```

Alura-Imersao-Dados-Python-II/
│
├── App.py
├── dados-imersao-final.csv
├── requirements.txt
└── README.md

```

---

## ▶️ Como Executar

1. Clone o repositório
git clone https://github.com/MCLG1661/Alura-Imersao-Dados-Python-II.git

Entre no diretório:

cd Alura-Imersao-Dados-Python-II

2. Crie um ambiente virtual
Windows
python -m venv .venv
.venv\Scripts\activate
Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

3. Instale as dependências
pip install -r requirements.txt

4. Execute a aplicação
streamlit run App.py

O Streamlit abrirá o dashboard no navegador.

---

## 💡 Competências Demonstradas

- Data Analytics
análise exploratória;
indicadores;
ag
regações;
filtros;
análise salarial;
interpretação de dados.

- Python
Pandas;
DataFrames;
GroupBy;
filtros booleanos;
funções;
cache;
tratamento de dados vazios.

- Data Visualization
gráficos de barras;
histogramas;
gráficos de rosca;
mapas coropléticos;
Plotly.

- Data Apps
Streamlit;
sidebar;
multiselect;
métricas;
componentes interativos;
DataFrames;
UX analítica.

- Engenharia
Git;
GitHub;
requirements.txt;
organização de projeto;
documentação técnica.

---

## 💼 Possíveis Aplicações

Embora o dataset seja salarial, a arquitetura do projeto pode ser adaptada para diferentes contextos.

Marketing Analytics
Campanhas
   ↓
Filtros
   ↓
KPIs
   ↓
Visualizações
   ↓
Dashboard
Vendas
Clientes
   ↓
Receita
   ↓
Produtos
   ↓
Regiões
   ↓
Data App
RH / People Analytics
Profissionais
   ↓
Senioridade
   ↓
Salários
   ↓
Localização
   ↓
Indicadores
Operações
Dados Operacionais
   ↓
Indicadores
   ↓
Filtros
   ↓
Monitoramento

---

## 🚀 Possíveis Evoluções

O projeto pode evoluir com:

deploy público no Streamlit Community Cloud;
filtros adicionais;
comparação entre países;
análise temporal;
boxplots por senioridade;
métricas de mediana;
análise por tecnologia;
exportação de dados filtrados;
testes automatizados;
modularização do código;
configuração externa;
logging;
cache avançado;
conexão com banco de dados;
API;
Power BI como camada complementar.

---

## ⚠️ Limitações

Este projeto possui finalidade educacional e demonstrativa.

A aplicação:

utiliza um dataset específico;
não realiza previsão salarial;
não representa necessariamente todo o mercado de trabalho em Dados;
não possui backend;
não possui autenticação;
não possui banco de dados;
não implementa Machine Learning;
depende da qualidade e cobertura do dataset utilizado.

O foco está na construção de uma experiência de Data Analytics interativa.

---

## 🎓 Contexto Acadêmico

Projeto desenvolvido durante a Imersão Python com Dados II — Alura.

A imersão permitiu aplicar conceitos de análise de dados, manipulação de DataFrames e visualização na construção de uma aplicação interativa voltada ao usuário final.

---

## 🙏 Agradecimentos

Alura
Guilherme Lima
Vinícius Caridá
Marcell Almeida
Valquíria Alencar
Comunidade Python

---

## 👨‍💻 Autor

Marcus Guedes

Marketing | Data Science | Inteligência Artificial | Gestão de Projetos

GitHub: MCLG1661
LinkedIn: Marcus Guedes

📊 Transformando dados em experiências analíticas interativas.
