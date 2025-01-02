# Módulo 4 - Meu Primeiro Modelo com Scikit-Learn

O objetivo deste módulo é colocar a "mão na massa" e desenvolver um primeiro modelo de machine learning, com o objetivo de reforçar alguns conceitos apresentados no módulo de fundamentos de machine learning, bem como fazer uma exploração inicial da biblioteca Scikit-learn que nos acompanhará em boa parte da trilha.

## Tópicos principais

- O que é a biblioteca Scikit-learn
- Descrição do problema
- Carga de Dados
- Engenharia de Features
- Visualização dos Dados
- Separar Dados de Treino e Teste
- Treinamento do Modelo
- Validação do Modelo
- Visualizar métricas do Modelo

### O que é a biblioteca Scikit-learn

O scikit-learn é uma biblioteca popular de aprendizado de máquina para a linguagem de programação Python. Ele fornece uma ampla variedade de ferramentas e algoritmos para tarefas de aprendizado de máquina, como classificação, regressão, clusterização, redução de dimensionalidade e muito mais. O scikit-learn é conhecido por sua facilidade de uso, documentação abrangente e integração bem com outras bibliotecas Python, como NumPy, pandas e matplotlib. É uma escolha popular entre cientistas de dados e desenvolvedores para criar modelos de aprendizado de máquina e realizar análises de dados.

### Descrição do problema

Um laboratório de análises clínicas, com base em dados de pacientes que realizaram exames de diabetes, gostaria de prever, com base em características como idade, peso e altura, qual o resultado esperado do exame para novos pacientes.

Para isso, iremos treinar um algoritmo supervisionado (dado que temos dados reais dos resultados) para criar um modelo preditivo que atenda à necessidade deste laboratório.