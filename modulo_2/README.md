# Módulo 2 - Aplicando EDA com pandas

O objetivo da Análise Exploratória de Dados (EDA - Exploratory Data Analysis) é dar uma boa espiada nos dados antes de começar a fazer coisas mais complicadas. É como o investigador curioso que olha primeiro para entender do que se trata. A análise ajuda a descobrir segredos escondidos nos números, padrões estranhos e até erros, para que possamos tomar decisões mais inteligentes e contar histórias mais interessantes com nossos dados. É como a primeira pista em um quebra-cabeça gigante de informações.

## Tópicos principais:

- O que é EDA?
- O que é a biblioteca Pandas?
- Coleta e Preparação de Dados
- Lidando com dados ausentes
- Formulando hipóteses 
- Análise Univariada
- Análise Bivariada
- Lidando com Outliers
- Automatizando EDA

### O que é EDA?

EDA é um processo sistemático usado em projetos de ciência de dados para entender e resumir as características fundamentais de um conjunto de dados.

A primeira etapa consiste em coletar e preparar os dados seja de banco de dados, arquivos, etc. Após isso é possível formular hipóteses que serão testadas a partir de análises univariadas, bivariadas, multivariadas e temporais.

Após isso é necessário comunicar os resultados de forma clara.

Em todos os processos é necessário lidar com valores ausentes e outliers.

### O que é a biblioteca Pandas?

O Pandas é uma biblioteca de Python amplamente usada para análise de dados. Sua principal vantagem é sua capacidade de manipular, limpar e analisar dados de forma eficiente. Ele fornece estruturas de dados flexíveis, como Series e DataFrames, que permitem organizar dados em tabelas, realizar operações complexas, como filtros e agregações, e facilitar a visualização dos resultados. O Pandas também é compatível com várias fontes de dados, como arquivos CSV, Excel, e bancos de dados, tornando-o essencial para cientistas de dados e analisstas que desejam explorar e extrair insights de dados de maneira eficaz e intuitiva.

### O contexto do nosso problema

O contexto que iremos analisar neste módulo de Análise Exploratória é do segmento de telecom. A empresa possui três conjuntos de dados de clientes e serviços, com uma variável que determina se o cliente abandonou (churn) ou não a empresa de telecom.

O intuito é que com estes conjuntos de dados e com base em algumas hipóteses que iremos formular e que serão respondidas pelo EDA, possa obter alguns insights iniciais para a construção de inteligência artificial que possa "prever" o abandono de clientes ainda ativos.