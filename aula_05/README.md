# Projeto 01: Um Bilhão de Linhas  
### Desafio de Processamento de Dados com Python

Este projeto tem como objetivo demonstrar como processar eficientemente um arquivo massivo contendo **1 bilhão de linhas** (aproximadamente 14GB), utilizando Python para realizar operações estatísticas pesadas como **agregação** e **ordenação**.

Inspirado no desafio original *The One Billion Row Challenge*, proposto para Java, esta versão foca em soluções Python para lidar com grandes volumes de dados de forma otimizada.

## Sobre os dados

O arquivo de entrada contém registros de medições de temperatura de diversas estações meteorológicas. Cada linha segue o formato:
<nome da estação>;<medição de temperatura>


A temperatura é registrada com uma casa decimal de precisão.

## Objetivo do processamento

O programa deve ser capaz de:
- Ler o arquivo completo de forma eficiente
- Calcular, para cada estação:
  - Temperatura mínima
  - Temperatura média (com arredondamento para uma casa decimal)
  - Temperatura máxima
- Exibir os resultados em uma tabela ordenada alfabeticamente pelo nome da estação

Este projeto é uma excelente oportunidade para aplicar técnicas de manipulação de dados em larga escala, otimização de desempenho e uso inteligente de estruturas como dicionários, agregadores e ordenadores em Python.