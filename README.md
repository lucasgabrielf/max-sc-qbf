# Max Set Cover Quadratic Binary Function Problem (MAX-SC-QBF)

O problema **MAX-SC-QBF** consiste em maximizar uma função quadrática binária sujeita a restrições de cobertura de conjuntos, onde o universo a ser coberto é o próprio conjunto de variáveis da função.

* Seja $N = {1, \dots, n}$ o conjunto de variáveis.

* Seja $S = {S_1, \dots, S_n}$ uma coleção de subconjuntos $S_i \subseteq N$, representando os elementos que o subconjunto $i$ cobre.

Cada subconjunto $S_i$ está associado a uma variável binária $x_i$, que indica se o subconjunto foi selecionado ou não.

Para cada par $(i,j)$ de subconjuntos, existe um coeficiente $a_{ij} \in \mathbb{R}$ que representa o ganho (positivo ou negativo) ao selecionar ambos simultaneamente.

O objetivo é escolher subconjuntos de forma que todas as variáveis de $N$ sejam cobertas, ou seja, para todo $k \in N$, exista ao menos um subconjunto $S_i$ tal que $k \in S_i$ e $x_i = 1$, e ainda buscando maximizar o ganho quadrático total, derivado das interações entre subconjuntos selecionados.

Mais formalmente, o problema pode ser definido como: dado o conjunto de variáveis $N=\\{{1,\dots,n\\}}$, uma coleção de subconjuntos $S=\\{S_1,\dots,S_n\\}$ com $S_i \subseteq N$, variáveis binárias $x_i$ indicando a seleção de $S_i$, e coeficientes $a_{ij} \in \mathbb{R}$ que modelam o ganho pela seleção conjunta de $(i,j)$, formulamos:

**Função Objetivo**

$$
\sum_{i=1}^{n}\sum_{j=1}^{n} a_{ij}\,x_i x_j
$$

**Sujeito a (cobertura)**

$$
\sum_{i:\, k \in S_i} x_i \ge 1, \quad \forall\, k \in N
$$

**Domínio**

$$
x_i \in \{0,1\}, \quad \forall\, i \in N
$$
