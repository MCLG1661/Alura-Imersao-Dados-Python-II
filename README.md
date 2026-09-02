# 📊 Dashboard de Análise de Salários na Área de Dados

> Data App interativo desenvolvido com **Python, Pandas, Streamlit e Plotly** para explorar salários, senioridade, contratos, modalidades de trabalho e distribuição geográfica de profissionais da área de Dados.

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

- Data Analytics;
- Data Visualization;
- Pandas;
- Streamlit;
- Plotly;
- DataFrames;
- KPIs;
- filtros;
- agregações;
- dashboards;
- Data Apps;
- UX aplicada a dados.

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

```text
Ano
Senioridade
Tipo de Contrato
Tamanho da Empresa
```

Os filtros são aplicados simultaneamente ao DataFrame:

```python
df_filtrado = df[
    (df["ano"].isin(anos_selecionados))
    & (df["senioridade"].isin(senioridades_selecionadas))
    & (df["contrato"].isin(contratos_selecionados))
    & (df["tamanho_empresa"].isin(tamanhos_selecionados))
]
```

Isso permite ao usuário alterar dinamicamente o recorte da análise.

---

## 📌 KPIs

O dashboard apresenta quatro indicadores principais:

```text
Salário Médio
Salário Máximo
Total de Registros
Cargo Mais Frequente
```

As métricas são recalculadas automaticamente de acordo com os filtros aplicados.

Caso nenhuma observação corresponda à combinação selecionada, a aplicação trata o DataFrame vazio e apresenta valores padrão, evitando falhas na interface.

---

## 📊 Visualizações

### 1. Top 10 cargos por salário médio

Gráfico de barras horizontais que apresenta os dez cargos com maior média salarial dentro do recorte selecionado.

```text
DataFrame Filtrado
        ↓
GroupBy por Cargo
        ↓
Média Salarial
        ↓
Top 10
        ↓
Plotly Bar Chart
```

---

### 2. Distribuição dos salários

Histograma que representa a distribuição dos salários anuais em USD.

A visualização ajuda a observar:

- concentração;
- dispersão;
- faixas salariais;
- assimetrias;
- valores extremos.

---

### 3. Modalidade de trabalho

Gráfico de rosca que apresenta a distribuição das modalidades de trabalho presentes no dataset.

A análise utiliza a contagem das ocorrências para calcular a participação de cada modalidade.

---

### 4. Salário médio de Data Scientist por país

Mapa coroplético que apresenta o salário médio de profissionais classificados como **Data Scientist** por país.

```text
DataFrame
    ↓
Filtro: Data Scientist
    ↓
GroupBy por País
    ↓
Média Salarial
    ↓
Choropleth
```

Caso não existam registros de Data Scientist para os filtros selecionados, a aplicação apresenta uma mensagem informativa em vez de tentar gerar um gráfico vazio.

---

## 🗂️ Dados Detalhados

Além dos KPIs e gráficos, o dashboard apresenta o DataFrame resultante dos filtros.

Isso permite ao usuário visualizar diretamente os registros que sustentam as métricas e visualizações apresentadas.

---

## ⚙️ Carregamento dos Dados

O projeto utiliza o dataset armazenado no próprio repositório:

```text
dados-imersao-final.csv
```

O carregamento utiliza cache do Streamlit:

```python
@st.cache_data
def carregar_dados():
    return pd.read_csv("dados-imersao-final.csv")

df = carregar_dados()
```

O uso de `st.cache_data` evita a leitura desnecessária do arquivo CSV a cada interação com os componentes da aplicação.

---

## 🛡️ Tratamento de Edge Cases

A aplicação contempla cenários em que a combinação dos filtros retorna zero registros.

Nesse caso:

```text
Salário médio         → 0
Salário máximo        → 0
Total de registros    → 0
Cargo mais frequente  → N/A
```

Os gráficos e a tabela também verificam se existem dados antes da renderização.

Essa abordagem evita erros durante a navegação e melhora a experiência do usuário.

---

## 🧠 Arquitetura da Aplicação

```text
┌─────────────────────────┐
│       Dataset CSV       │
│     Dados Salariais     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│         Pandas          │
│ DataFrame + Tratamento  │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│         Filtros         │
│   Recorte dos Dados     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│    KPIs + Agregações    │
│     Análise de Dados    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│         Plotly          │
│ Visualizações Interativas│
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       Streamlit         │
│ Interface + Interação   │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│        Usuário          │
│ Exploração Analítica    │
└─────────────────────────┘
```

---

## 🛠️ Tecnologias

| Tecnologia | Aplicação |
|---|---|
| **Python** | Linguagem principal |
| **Pandas** | Manipulação, filtragem e análise dos dados |
| **Streamlit** | Interface e construção do Data App |
| **Plotly** | Visualizações interativas |
| **CSV** | Fonte de dados |
| **Git** | Controle de versão |
| **GitHub** | Repositório e documentação |

---

## 📂 Estrutura do Projeto

```text
Alura-Imersao-Dados-Python-II/
│
├── App.py
├── dados-imersao-final.csv
├── requirements.txt
└── README.md
```

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/MCLG1661/Alura-Imersao-Dados-Python-II.git
```

### 2. Entre no diretório

```bash
cd Alura-Imersao-Dados-Python-II
```

### 3. Crie um ambiente virtual

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
streamlit run App.py
```

O Streamlit iniciará a aplicação e disponibilizará o dashboard no navegador.

---

## 📦 Dependências

O projeto utiliza:

```text
pandas==2.2.3
streamlit==1.44.1
plotly==5.24.1
```

---

## 💡 Competências Demonstradas

### Data Analytics

- análise exploratória;
- criação de indicadores;
- agregações;
- filtros;
- análise salarial;
- interpretação de dados.

### Python

- Pandas;
- DataFrames;
- `groupby`;
- filtros booleanos;
- funções;
- cache;
- tratamento de DataFrames vazios.

### Data Visualization

- gráficos de barras;
- histogramas;
- gráficos de rosca;
- mapas coropléticos;
- visualizações interativas com Plotly.

### Data Apps

- Streamlit;
- sidebar;
- multiselect;
- métricas;
- componentes interativos;
- apresentação de DataFrames;
- UX aplicada à análise de dados.

### Engenharia

- Git;
- GitHub;
- gerenciamento de dependências;
- organização de projeto;
- documentação técnica.

---

## 💼 Possíveis Aplicações

Embora o projeto utilize dados salariais, a mesma arquitetura pode ser adaptada para diferentes cenários de negócio.

### Marketing Analytics

```text
Campanhas
    ↓
Filtros
    ↓
KPIs
    ↓
Visualizações
    ↓
Dashboard
```

### Vendas

```text
Clientes + Produtos + Receita
              ↓
            Pandas
              ↓
             KPIs
              ↓
          Dashboard
```

### People Analytics

```text
Profissionais
      ↓
Senioridade
      ↓
Salários
      ↓
Localização
      ↓
Indicadores
```

### Operações

```text
Dados Operacionais
        ↓
Indicadores
        ↓
Filtros
        ↓
Visualizações
        ↓
Monitoramento
```

---

## 🚀 Possíveis Evoluções

O projeto pode evoluir com:

- deploy público;
- filtros adicionais;
- comparação salarial entre países;
- análise temporal;
- salário mediano;
- boxplots por senioridade;
- análise por cargo;
- exportação dos dados filtrados;
- testes automatizados;
- modularização da aplicação;
- logging;
- conexão com banco de dados;
- consumo de API;
- Power BI como camada analítica complementar.

Uma evolução interessante seria separar a aplicação em diferentes camadas:

```text
Data Source
    ↓
Data Processing
    ↓
Analytics
    ↓
Visualization
    ↓
User Interface
```

---

## ⚠️ Limitações

Este projeto possui finalidade educacional e demonstrativa.

A aplicação:

- utiliza um dataset específico;
- não realiza previsão salarial;
- não representa necessariamente todo o mercado de trabalho em Dados;
- não implementa Machine Learning;
- não possui autenticação;
- não possui banco de dados;
- depende da qualidade e cobertura do dataset utilizado.

O foco do projeto está na construção de uma experiência de **Data Analytics interativa com Python**.

---

## 🎓 Contexto Acadêmico

Projeto desenvolvido durante a **Imersão Python com Dados II — Alura**.

A imersão permitiu aplicar conceitos de análise e manipulação de dados na construção de uma aplicação interativa, aproximando o processamento realizado em Python de uma experiência voltada ao usuário final.

---

## 🙏 Agradecimentos

Agradecimentos à **Alura** e aos professores:

- Guilherme Lima
- Vinícius Caridá
- Marcell Almeida
- Valquíria Alencar

E à comunidade Python e aos mantenedores das bibliotecas utilizadas no projeto.

---

## 👨‍💻 Autor

**Marcus Guedes**

Marketing | Data Science | Inteligência Artificial | Gestão de Projetos

- **GitHub:** [MCLG1661](https://github.com/MCLG1661)
- **LinkedIn:** [Marcus Guedes](https://www.linkedin.com/in/marcusguedes/)

---

📊 **Transformando dados em experiências analíticas interativas.**
