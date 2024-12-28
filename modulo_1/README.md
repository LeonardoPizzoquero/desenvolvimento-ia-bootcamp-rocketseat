# Módulo 1 - Medidas, Dispersão, COrrelação e Gráficos

O módulo 1 apresenta tópicos importantes sobre estatística, sendo explicados abaixo e aplicados na prática pelos scripts contidos em: main.ipynb 

## Tópicos principais:

- O que é estatística

- População e amostra

- Tipos de variáveis

- Teorema do limite central

- Medidas de posição

- Medidas de dispersão

- Medidas de Forma

- Correlação

- Representações Gráficas

## O que é estatística?

A estatística é a ciência que trata da coleta, organização, análise e interpretação de dados. Ela é usada em diversas áreas, como negócios, ciência, engenharia, governo e medicina.

A estatística é uma ferramenta poderosa que pode ser usada para tomar decisões informadas. Por exemplo, uma empresa pode usar a estatística para prever a demanda por um produto, um cientista pode usar a estatística para testar a eficácia de um tratamento e um governo pode usar a estatística para avlaiar a efetividade de uma política pública.

### Áreas da estatística:

**Probabilidade:** Área que estuda as chances de eventos aleatórios ocorrerem. Ela é usada para medir a incerteza de eventos, e para fazer previsões sobre o futuro. Ex: Probabilidade de ações caírem ou subirem na próxima hora.

**Estatística descritiva:** É o ramo da estatística que envolve a coleta, organização e resumo dos dados, revelando padrôes, tendências e características dos mesmos, sem fazer inferências sobre populações maiores.

**Inferência estatística:** É a prática de tirar conclusões ou fazer previsões sobre uma população maior com base em dados de uma amostra representativa, usando métodos estatísticos e probabilísticos.

### População e amostra:

**População:** Se refere a todo o conjunto de elementos que compartilham uma característica comum. Por exemplo, se estamos interessados nas alturas de todas as pessoas em um país, a população seria todas as alturas de todas as pessoas no país.

**Amostra:** Uma amostra, por outro lado, é um subconjunto selecionado da população. É inviável ou impraticável medir ou analisar todas as unidades na população, então usamos uma amostra representativa para fazer inferências ou generealizações sobre a população maior.

A amostragem envolve a seleção cuidadosa de um grupo menor de elementos que deve ser representativo das características da população, permitindo-nos fazer estimativas sobre a população inteira com base nas informações da amostra.

### Tipos de variáveis:

As variáveis se dividem em dois grandes grupos, quantitativas (números) e qualitativas (categorias).

**Subtipos da quantitativa:** Contínuas (intervalo contínuo, ex: altura, salário, inflação) e discretas (valores inteiros, idade, numero de empregados, produção de veículos)

**Subtipos da qualitativa:** Nominais (sem ordem, ex: raça/cor, sexo, profissão) e ordinais (com ordem, ex: escolaridade, faixa etária, ranking de reclamações).

### Teorema do limite central

É um dos principais teoremas da estatística que diz que, quando você pega várias amostras aleatórias de uma população e calcula a média de cada uma, independentemente da forma da distribuição original, essas médias se aproximam de uma distribuição normal ou gaussiana (formato de sino) à medida que o tamanho das amostras aumenta.

O teorema do limite central é importante porque nos permite fazer inferências sobre a população com base em uma amostra. Por exemplo, se você sabe que a distribuição da média amostral é normal, você pode usar uma tabela de distribuição normal para calcular a probabilidade de que a média amostral seja maior ou menor que um determinado valor.

### Medidas de Posição

Apresentão como os dados estão distribuídos com relação a uma medida central

**Média:** É a soma de todos os valores dividida pelo número de valores. É a medida mais comum de tendência central. No entanto, ela pode ser sensível a valores extremos.

**Mediana:** É o valor que divide o conjunto de dados em duas partes iguais. Em outras palavras, é o valor do meio quando os dados estão ordenados. A mediana não é influenciada por valores extremos e é útil em distribuições assimétricas.

**Moda:** É o valor que ocorre com mais frequência em um conjunto de dados. Pode haver uma ou mais modas, ou o conjunto pode não ter uma moda. A moda é útil em dados categóricos ou quando se deseja identificar os valores mais frequentes.

## Medidas de Dispersão

**Variância:** É a média dos quadrados das diferenças entre cada valor e a média aritmética. Ela fornece uma ideia de quão distantes os valores estão da média, considerando o peso de cada diferença ao quadrado.

**Desvio padrão:** É a raiz quadrada da variância. Ele expressa a dispersão em termos da mesma unidade dos dados e é uma medida de dispersão mais comum.

**Coeficiente de Variação:** É o desvio padrão dividido pela média, expresso como porcentagem. Ele indica a variabilidade relativa dos dados em relação à média e é útil para comparar a dispersão entre conjuntos de dados diferentes.

## Medidas de Forma

**Assimetria:** Indica o grau e a direção da distorção da distribuição em relação à média. Uma assimetria positiva significa que a cauda direita da distribuição é mais longa (os valores maiores estão mais espalhados), enquanto uma assimetria negativa significa que a cauda esquerda é mais longa.

**Curtose:** Mede o pico ou a "pontuação" da distribuição. Uma curtose alta indica uma distribuição mais concentrada (pico mais agudo e caudas mais pesadas), enquanto uma curtose baixa indica uma distribuição mais achatada (pico menos agudo e caudas menos pesadas).

### Curtose

**Mesocúrtica**: A própria curva normal padrão

**Platicúrtica**: Possui grau de achatamento maior que da curva normal padrão, o que nos indica que os dados estão mais espalhados (logo, o desvio padrão também é maior)

**Leptocúrtica**: Seu grau de achatamento é menor que o da curva normal padrão (curva mais pontiaguda), indica que os dados estão mais concentrados (desvio padrão menor).


## Correlação

A correlação na estatística mede a relação entre duas variáveis, indicando se elas têm uma associação linear positiva (aumentam juntas), negativa (uma aumenta enquanto a outra diminui) ou nenhuma correlação. A importância para algoritmos de Machine Learning reside na capacidade de identificar padrões e relações entre variáveis. A correlação ajuda a selecionar características relevantes para os modelos, melhorando a precisão interpretabilidade. Também permite ajustar modelos para prever com maior acurácia com base nas relações observadas nos dados.

### Coeficientes

**Coeficiente de Pearson**: Mede a relação linear entre duas variáveis, variando de -1 (correlação negativa perfeita) a 1 (correlação positiva perfeita), e 0 para nenhuma correlação. Adequado para variáveis numéricas que possam ter uma relação linear.

**Coeficiente de Spearman**: Avalia a relação monotônica (não necessariamente linear) entre variáveis, usando uma escala similar ao Pearson. É útil quando os dados não têm uma relação linear clara ou quando as variáveis não são numericamente escalonáveis.

## Representações Gráficas

### Histograma

É usado para variáveis numéricas contínuas, mostrando a distribuição dos dados em intervalos.

### Gráfico de barras

Aplicável a variáveis categóricas ou discretas, exibindo a contagem ou frequência de cada categoria. Usar as barras horizontais quando há ranking dos dados, por exemplo quantidade de empresas por estados.

### Gráfico de dispersão

Usado para mostrar a relação entre duas variáveis numéricas, ajudando a identificar padrões ou tendências.

### Box Plot (Diagrama de Caixa)

Adequado para variáveis numéricas ou categóricas ordinais, revelando distribuição, mediana e valores atípicos.

### Gráfico de linhas

Utilizado para variáveis numéricas ao longo do tempo ou em uma sequência, destacando tendências temporais.