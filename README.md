# Health-Insurance-Cross-sell

![code](https://img.shields.io/static/v1?label=python&message=3.8&color=blue) ![license](https://img.shields.io/static/v1?label=license&message=MIT&color=<COLOR>) ![version](https://img.shields.io/static/v1?label=version&message=1.0&color=yellow) ![api](https://img.shields.io/static/v1?label=api&message=flask&color=red) ![deploy](https://img.shields.io/static/v1?label=deploy&message=heroku&color=orange) ![webapp](https://img.shields.io/static/v1?label=deploy&message=streamlit&color=purple)

Previsão de interesse em um seguro de automóvel.

<p align="center">
  <img src="img/insurance.jpg" width="1000" title="img-principal">
</p>

# Conteúdo

<!--ts-->

1.  [Contexto do Problema](Contexto-do-Problema)
2.  [O Problema](O-Problema)
3.  [Entendimento do Problema](Entendimento-do-Problema)
4.  [Dados](Descrição-de-Dados)
5.  [Planejamento da Solução](Planejamento-da-Solução)
6.  [Premissas Assumidas](Premissas-Assumidas)
7.  [Hipóteses Principais](Hipóteses-Principais)
8.  [Algoritmos ML](Algoritmos-de-Machine-Learning-Aplicados)
9.  [Performace Modelos](Performace-dos-Modelos-de-Machine-Learning)
10. [Resultados](Resultados)
11. [Entrega da Solução](#Entrega-da-Solucao)

<!--te-->

# Contexto do Problema

A **Insurance All** é uma empresa que fornece seguro de saúde para seus clientes e o time de produtos está analisando a possibilidade de oferecer aos assegurados, um novo produto: Um seguro de automóveis.

Assim como o seguro de saúde, os clientes desse novo plano de seguro de automóveis precisam pagar um valor anualmente à Insurance All para obter um valor assegurado pela empresa, destinado aos custos de um eventual acidente ou dano ao veículo.

A Insurance All fez uma pesquisa com cerca de 380 mil clientes sobre o interesse em aderir a um novo produto de seguro de automóveis, no ano passado. Todos os clientes demonstraram interesse ou não em adquirir o seguro de automóvel e essas respostas ficaram salvas em um banco de dados junto com outros atributos dos clientes.

O time de produtos selecionou 127 mil novos clientes que não responderam a pesquisa para participar de uma campanha, no qual receberão a oferta do novo produto de seguro de automóveis. A oferta será feita pelo time de vendas através de ligações telefônicas.

Contudo, o time de vendas tem uma capacidade de realizar 20 mil ligações dentro do período da campanha.

# O Problema

Nesse contexto, você foi contratado como um consultor de Ciência de Dados para construir um modelo que prediz se o cliente estaria ou não interessado no seguro de automóvel.

Com a sua solução, o time de vendas espera conseguir priorizar as pessoas com maior interesse no novo produto e assim, otimizar a campanha realizando apenas contatos aos clientes mais propensos a realizar a compra.

Como resultado da sua consultoria, você precisará entregar um relatório contendo algumas análises e respostas às seguintes perguntas:

1. Principais Insights sobre os atributos mais relevantes de clientes interessados em adquirir um seguro de automóvel.

2. Qual a porcentagem de clientes interessados em adquirir um seguro de automóvel, o time de vendas conseguirá contatar fazendo 20.000 ligações?

3. E se a capacidade do time de vendas aumentar para 40.000 ligações, qual a porcentagem de clientes interessados em adquirir um seguro de automóvel o time de vendas conseguirá contatar?

4. Quantas ligações o time de vendas precisa fazer para contatar 80% dos clientes interessados em adquirir um seguro de automóvel?

# Entendimento do Problema

**Motivação:**

- A empresa vai realizar uma campanha para um novo produto (seguro de automóvel).

**Causa Raiz do Problema:**

- Identificar clientes com maior interesse no seguro do automóvel.

**Dados para Resolver o Problema:**

- Os dados estão armazenados em um banco de dados PostgresSQL na AWS

**Formato da Solução:**

- **Granularidade:** Previsão da probabilidade de compra por cliente.
- **Tipo de Problema:** Previsão da probabilidade de compra.
- **Potênciais Métodos:** Ranqueamento, Classificação.
- **Formato da Entrega:** WebApp Streamlit.

# Descrição de Dados

O Dataset usado para este projeto possui 381109 linhas e 12 colunas. Os dados contém:

| Atributo           | Significado                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------- |
| id                 | Unique ID for the customer                                                                |
| Gender             | Gender of the customer                                                                    |
| Age                | Age of the customer                                                                       |
| Driving_License    | 0 : Customer does not have DL, 1 : Customer already has DL                                |
| Region_Code        | Unique code for the region of the customer                                                |
| Previously_Insured | 1 : Customer already has Vehicle Insurance, 0 : Customer doesn't have Vehicle Insurance   |
| Vehicle_Age        | Age of the Vehicle                                                                        |
| Vehicle_Damage     | 1 : Customer got his/her vehicle damaged. 0 : Customer didn't get his/her vehicle damaged |
| Annual_Premium     | The amount customer needs to pay as premium in the year                                   |
| PolicySalesChannel | iAnonymized Code for the channel of outreaching to the customer ie.                       |
| Vintage            | Number of Days, Customer has been associated with the company                             |
| Response           | Customer is interested, 0 : Customer is not interested                                    |

# Planejamento da Solução

**1. Descrever os Dados:**

- Carregar o conjunto de dados que será utlizado, entender as variáveis disponíveis e verificar possíveis valores faltantes e inconsistências.
- Realizar uma estatística descritiva para entender as características dos dados.

**2. Levantar Hipóteses:**

- Criar Hipóteses sobre as características e o comportamento de venda nas lojas.
- Realizar um Feature Engineering para criar novas variáveis.

**3. Filtrar Dados:**

- Filtrar linhas e colunas de acordo com as restrições de negócio e com as premissas assumidas.

**4. Realizar Análise Exploratória de Dados:**

- Validar ou refutar as hipóteses através dos dados.
- Identificar correlação entre variáveis e a variável resposta.
- Obter insights.

**5. Preparar os dados**

- Fazer o reescalonamento das variáveis, aplicar Encoding e transformar os dados

**6. Selecionar as melhores Features**

- Aplicar o algoritmo Boruta para seleção de Features e adicionar os resultados com as variaveis julgadas importantes na fase de análise exploratória.

**7. Modelagem de Machine Leaning**

- Treinar, validar e aplicar cross validation nos algoritmos de média móvel, Regressão linear, Regressão Linear Regularizada, Random Forest Regressor e XGboost Regressor.

**8. Ajustar os Hiperparametros**

- Encontrar a melhor combinação de parametros para o modelo final usando a técnica de Random Search.

**9. Traduzir e Interpretar o erro**

- Transformar a performace de Machine Leaning para resultado de Negócio e trazer cenários da predição para auxilar a tomada de decisão do CFO.

**10. Deploy do Modelo em Produção**

- Deixar o modelo acessível para o CFO acessar os resultados do modelo de qualquer lugar.

# Premissas Assumidas

# Hipóteses Principais

# Algoritmos de Machine Learning Aplicados

Os modelo treinados foram:

- kNN
- Logistic Regression
- Random Forest
- XGBoost
- Naive Bayes

O modelo escolhido para resolver o problema de Insurance All foi:

- XGBoost.

# Performace dos Modelos de Machine Learning

As métricas usadas para comparação dos resultados foram: Precision top k (Precision @k), Recall topk (Recall @k), curva lift e curva acumulativa de ganho. Os resultados das performaces obtidas com a validação cruzada foram:

| Model Name          | precision_top_20000 | recall_top_20000 |
| ------------------- | ------------------- | ---------------- |
| XGBoost             | 0.279046            | 0.932077         |
| Random Forest       | 0.276826            | 0.924927         |
| Naive Bayes         | 0.2726863           | 0.911096         |
| KNN                 | 0.270036            | 0.902008         |
| Logistic Regression | 0.265747            | 0.887909         |

# Resultados

## Respondendo Perguntas do Negócio

# Entrega da Solução

## Arquitetura Modelo em Produção

## Demonstração do Modelo
