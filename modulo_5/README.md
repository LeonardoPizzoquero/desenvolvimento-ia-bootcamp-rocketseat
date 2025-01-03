# Módulo 5 - Algoritmos Supervisionados

O objetivo deste módulo é apresentar conceitualmente os principais algoritmos de regressão para que possamos desenvolver projetos de machine learning que fazem previsões de valores. E faremos um projeto explorando o primeiro destes algoritmos, que é o de regressão linear simples, onde faremos o processo completo desde o EDA até a entrega do modelo através de uma API para consumo por outras aplicações.

## Tópicos principais

- O que é uma análise de regressão?
- Um passeio pelos tipos de regressão
- Projeto - Regressão Linear Simples

## O que é uma análise de regressão?

A análise de regressão é uma abordagem estatística que busca investigar e quantificar as relações entre variáveis. Ela é usada para entender como uma variável dependente (target) está relacionada a uma ou mais variáveis independentes (fatores que acreditamos influenciar a variável dependente).

Essa técnica permite construir um modelo matemático, geralmente na forma de uma equação linear, que representa essa relação. Ao ajustar o modelo aos dados observados, podemos estimar os parâmetros e entender como as mudanças nas variáveis independentes afetam a variável dependente.

Isso é fundamental para fazer previsões, tomar decisões embasadas em evidências e compreender melhor os padrões em dados do mundo real.

## Um passeio pelos tipos de regressão

- Linear Simples: Envolve uma variável independente e uma variável dependente, sendo representada por uma linha reta. Exemplo: Prever pontuação num exame com base no tempo de estudo.

- Linear múltipla: Utiliza várias variáveis independentes para prever ua variável dependente, resultando em um modelo linear mais complexo. Exemplo: Prever desempenho de alunos com base em múltiplas variáveis.

- Logística: Usada geralmente para prever probabilidades em problemas de classificação (binária, multinomial, ordinal, aninhada) Exemplo: Prever se cliente fará compra online (sim/não).

- Polinomial: Permite modelar relações não-lineares entre as variáveis. A regressão polinomial usa uma curva (um polinômio) para se ajustar aos dados. Exemplo: Previsão de vendas de produtos com base no clima/temperatura.

- Poisson: Adequada para modelar dados de contagem, como o número de eventos em um determinado período. É comum em estudos epidemiológicos e de contagem. Exemplo: Número de Reclamações de Sinistros.

- Ridge, Lasso e ElasticNet: Técnicas de regularização para lidar com multicolinearidade e overfitting. São usadas em análises onde há muitas variáveis independentes. Exemplo: Estimar preços de casas com base em muitas variáveis.

- Gamma: Usada quando os dados não seguem uma distribuição normal e exibem uma assimetria positiva (à direita). Além disso, o target é contínuo e positivo. Exemplo: Previsão de tempo de permanência de pacientes em um hospital.

- Beta: Aplicada quando a variável dependente está restrita ao intervalo [0, 1], comum em análises de proporções e taxas. Exemplo: Taxa de conversão com base numa campanha de Mkt.

## Projeto - Regressão Linear Simples

Uma plataforma online de educação, que consegue acompanhar a quantidade de horas que seus alunos passam estudando numa determinada trilha, deseja avaliar se esta quantidade de horas influencia na pontuação do teste final.

Para isso, iremos treinar um algoritmo de regressão linear, de forma que seja possível prever a pontuação do teste final, dada a quantidade de horas de estudo.

### OLS: Ordinary Least Squares

O método dos mínimos quadrados ordinários (OLS) é uma técnica de otimização que estima os parâmetros de um modelo de regressão linear minimizando a soma dos quadrados das diferenças entre a variável dependente e as previsões do modelo.

Equação da regressão linear simples:

```
y = b0 + b1 * x
```

Onde:
- y: Variável dependente (pontuação do teste)
- b0: Intercepto
- b1: Coeficiente da variável independente (horas de estudo)

## API

Comando para rodar:

```
uvicorn modulo_5.api_regressao_linear_simples:app --reload
```

# Regressão Linear Múltipla

O objetivo deste módulo é apresentar o conceito de regressão linear múltipla, onde também iremos desenvolver um modelo através de um processo completo desde o EDA até a entrega do modelo através de uma UI para uso pelo usuário final.

## Tópicos principais

- O que é uma análise de regressão múltipla?
- Projeto - Regressão Linear Múltipla

## O que é uma análise de regressão múltipla?

A análise de regressão múltipla é uma extensão da análise de regressão linear simples, onde temos mais de uma variável independente para prever uma variável dependente.

O objetivo é entender como as variáveis independentes se relacionam com a variável dependente e como elas se relacionam entre si. Isso permite avaliar o impacto de cada variável independente na variável dependente, controlando os efeitos das outras variáveis.

A regressão múltipla é uma ferramenta poderosa para prever valores, identificar relações entre variáveis e entender melhor os padrões nos dados.

OLS: Ordinary Least Squares

O método dos mínimos quadrados ordinários (OLS) é uma técnica de otimização que estima os parâmetros de um modelo de regressão linear minimizando a soma dos quadrados das diferenças entre a variável dependente e as previsões do modelo.

Equação da regressão linear múltipla:

```	
y = b0 + b1 * x1 + b2 * x2 + ... + bn * xn
```

Onde:
- y: Variável dependente (pontuação do teste)
- b0: Intercepto
- b1, b2, ..., bn: Coeficientes das variáveis independentes (horas de estudo, horas de sono, etc.)

## Projeto - Regressão Linear Múltipla

Um laboratório de análises clínicas que conduz testes de colesterol, deseja avaliar, com base em características dos pacientes, tais como idade, nível de atividade física, peso, dentre outras, se estas variáveis influenciam no resultado do exame de colesterol total.

Para isso, iremos treinar um algoritmo de regressão linear múltipla, de forma que seja possível prever o resultado do exame de colesterol, dada as características do paciente.