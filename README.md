# 🧠 Desafio de Inteligência Artificial - Formação 4.0 | SENAC

Este repositório contém a resolução do desafio de IA proposto na Formação 4.0 do SENAC, onde o objetivo foi realizar análise, pré-processamento, modelagem e uso de um modelo preditivo com base em dados reais.

---

## 📊 Base de Dados Utilizada

Utilizamos o **Pima Indians Diabetes Database**, que está disponível publicamente no repositório do UCI Machine Learning:

- Link: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

### ✅ Justificativa para Escolha da Base

A base de dados foi escolhida foi escolhida por representar um problema real e relevante de saúde pública: a **detecção de diabetes tipo 2 em mulheres**. Originalmente, o conjunto de dados é do National Institute of Diabetes and Digestive and Kidney Diseases e contém informações clínicas de pacientes com pelo menos 21 anos, pertencentes à etnia Pima Indian. Essas características tornam a base específica, mas ainda representativa para estudos de aprendizado de máquina. 

- É uma base limpa e bem estruturada.
- É amplamente utilizada em projetos de aprendizado de máquina e benchmarks.
- Permite aplicar técnicas de classificação supervisionada com validação cruzada.
- Possui um número equilibrado de variáveis, facilitando a análise em um projeto introdutório sem ser trivial.

---

## 🔎 Etapa 1: Análise e Pré-processamento

Arquivo: `analise.ipynb`

- Carregamento e visualização da base de dados
- Verificação de valores nulos
- Análise estatística básica
- Gráficos para entender padrões e correlações
- Normalização e padronização dos dados
- Salvamento dos dados tratados em `dados_preprocessados.csv`

---

## 🤖 Etapa 2: Modelagem e Avaliação

Arquivo: `modelagem.ipynb`

- Importação dos dados pré-processados
- Separação dos dados em treino e teste
- Treinamento de dois modelos:
  - Regressão Logística
  - Árvore de Decisão
- Avaliação dos modelos com **validação cruzada**
- Comparação das médias de acurácia:
  - **Regressão Logística:** 76,4%
  - **Árvore de Decisão:** 69,3%
- Escolha do melhor modelo (Regressão Logística)
- Salvamento do melhor modelo em `melhor_modelo.pkl`

---

## 🔗 Acesso Público à Interface Gráfica

Para facilitar a demonstração do projeto, foi gerado um link temporário utilizando a funcionalidade `share=True` da biblioteca Gradio. Esse link permite o acesso à interface gráfica de predição sem necessidade de instalação local do projeto.

🔍 **Link para acesso público:** [https://59d7ea283d16b0d5be.gradio.live](https://59d7ea283d16b0d5be.gradio.live)  
⏳ **Disponibilidade:** O link ficará acessível por aproximadamente **1 semana**.

Essa interface permite inserir os dados de entrada do modelo e visualizar a predição diretamente pelo navegador.

---

## 🧪 Uso do Modelo com Script Python

Arquivo: `usar_modelo.py`

Este script:
- Carrega o modelo salvo com `pickle`
- Recebe novos dados e retorna a previsão de diabetes

Para rodar o script:

```bash
cd notebook
python usar_modelo.py


