# Max Set Cover Quadratic Binary Function Problem (MAX-SC-QBF)

The MAX-SC-QBF problem consists of maximizing a quadratic binary function subject to set cover constraints, where the universe to be covered is the set of variables itself.

* Let $N=\\{{1,\dots,n\\}}$ be the set of variables.

* Let $S=\\{S_1,\dots,S_n\\}$ be a collection of subsets $S_i \subseteq N$, representing the elements covered by subset $i$.

Each subset $S_i$ is associated with a binary variable $x_i$, indicating whether the subset is selected.

For each pair $(i,j)$ of subsets, there is a coefficient $a_{ij} \in \mathbb{R}$ that represents the gain (positive or negative) obtained by selecting both subsets simultaneously.

The goal is to select subsets such that all variables in $N$ are covered — that is, for every $k \in N$, there exists at least one subset $S_i$ such that $k \in S_i$ and $x_i = 1$ — while maximizing the total quadratic gain derived from the interactions among the selected subsets.

More formally, the problem can be defined as follows: given the set of variables $N=\\{{1,\dots,n\\}}$, a collection of subsets $S=\\{S_1,\dots,S_n\\}$ with $S_i \subseteq N$, binary variables $x_i$ indicating the selection of $S_i$, and coefficients $a_{ij} \in \mathbb{R}$ modeling the gain from jointly selecting $(i,j)$, we formulate:

**Objective Function**

$$
\sum_{i=1}^{n}\sum_{j=1}^{n} a_{ij}\,x_i x_j
$$

**Subject to (coverage)**

$$
\sum_{i:\, k \in S_i} x_i \ge 1, \quad \forall\, k \in N
$$

**Domain**

$$
x_i \in \\{0,1\\}, \quad \forall\, i \in N
$$
