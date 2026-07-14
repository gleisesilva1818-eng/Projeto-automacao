# 🤖 Automação de Cadastro de Produtos com Python

Este projeto é uma ferramenta de automação robótica de processos (RPA) desenvolvida em Python. O objetivo principal é otimizar o fluxo de trabalho operacional ao extrair dados de uma base de dados externa (arquivo CSV) e preencher automaticamente um sistema web de cadastro de produtos, simulando interações humanas (teclado e mouse) de forma rápida, eficiente e livre de erros manuais.

Projeto construído com base nos ensinamentos do treinamento prático ministrado pelo canal **Hashtag Programação**.

---

## 🚀 Tecnologias e Conceitos Utilizados

* **Python 3.12:** Linguagem base para o desenvolvimento do script de automação.
* **Pandas:** Biblioteca de alto desempenho utilizada para leitura, manipulação e análise da base de dados (`produtos.csv`).
* **PyAutoGUI:** Biblioteca de automação para simulação programática e controle de mouse, teclado e tela.
* **Controle de Fluxo e Loops:** Estrutura iterativa (`for`) para percorrer dinamicamente todas as linhas da tabela e cadastrar cada item de forma sequencial.

---

## 📋 Pré-requisitos e Instalação

Para executar este projeto localmente, você precisará ter o Python instalado em sua máquina e as dependências necessárias. Execute os comandos abaixo no seu terminal para instalar as bibliotecas obrigatórias:

```bash
pip install pandas openpyxl pyautogui
