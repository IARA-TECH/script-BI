# Script BI

Desenvolvimento de um **script Python para Business Intelligence (BI)**, voltado à **coleta, tratamento e integração de dados** provenientes de bancos de dados SQL.  

O projeto automatiza o processo de **extração e transformação de informações**, permitindo que sejam utilizadas em ferramentas de análise e visualização de dados.

---

## 📚 Sumário

* [💡 Sobre o Projeto](#-sobre-o-projeto)
* [⚙️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
* [🧩 Como Executar](#-como-executar)
* [🧰 Estrutura do Projeto](#-estrutura-do-projeto)
* [👩‍💻 Autor](#-autor)

---

## 💡 Sobre o Projeto

O **Script BI** foi desenvolvido com o objetivo de **automatizar o processo de extração e atualização de dados** utilizados em painéis de **Business Intelligence (BI)**.  

A aplicação permite:

* Executar **consultas SQL** pré-configuradas.  
* Realizar **tratamento e limpeza de dados** via Python.  
* Gerar dados prontos para análise em ferramentas como **Power BI** ou **Tableau**.  
* Configurar facilmente credenciais e parâmetros de conexão via arquivo `.env`.

---

## ⚙️ Tecnologias Utilizadas

| Categoria                         | Tecnologias / Ferramentas                         |
| --------------------------------- | ------------------------------------------------- |
| **Linguagem**                     | Python 3.9+                                       |
| **Banco de Dados**                | SQL (MySQL / PostgreSQL)                          |
| **Gerenciamento de Dependências** | `pip`, `requirements.txt`                         |
| **Automação / Scripts**           | `python-dotenv`, `pandas`, `psycopg2` ou `mysql-connector-python` |
| **Arquivos de Configuração**      | `.env` e `.env.example`                           |

---

## 🧩 Como Executar

### 🧱 Executando Localmente

```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/script-BI-main.git

# Acesse o diretório
cd script-BI-main

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
````

---

### ▶️ Executando o Script

Para rodar o processo de BI:

```bash
python script_bi.py
```
---

## 🧰 Estrutura do Projeto

```
script-BI-main/
├── .env.example        # Exemplo de variáveis de ambiente
├── .gitignore          # Arquivos ignorados pelo Git
├── script_bdInfo.sql   # Script SQL com consultas e criação de tabelas
└── script_bi.py        # Script principal de extração e tratamento de dados
```

---

## 👩‍💻 Autor
**IARA Tech**
Projeto Interdisciplinar desenvolvido por alunos do 1º e 2º ano de ensino médio do Instituto J&F, com o propósito de facilitar o registro e consulta de ábacos industriais.

📍 São Paulo, Brasil
📧 [iaratech.oficial@gmail.com](mailto:iaratech.oficial@gmail.com)
🌐 GitHub: [https://github.com/IARA-TECH](https://github.com/IARA-TECH)
