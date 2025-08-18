import numpy as np
import random

class MAXSCQBFGenerator:
    """
    Generates random instances of the MAX-SC-QBF problem.
    """
    def __init__(self):
        return
    
    def _generate_random_subsets(self, n, elements):
        # *Pattern 1: Generates purely random subsets.
        subsets = []
        used_elements = set()

        for _ in range(n):
            tamanho = random.randint(1, n)
            subset = sorted(random.sample(elements, k=tamanho))
            used_elements.update(subset)
            subsets.append(subset)
    
        elements_set = set(elements)
        avaiable = elements_set-used_elements
        if avaiable:
            for element in avaiable:
                subsets[random.randint(0, n-1)].append(element)
        return subsets

    def _generate_disjoint_groups_subsets(self, n, elements):
        # *Pattern 3: Creates some disjoint subsets, then fills randomly.
        subsets = []
        used_elements = set()
        num_disjoint = n // 3

        for _ in range(num_disjoint):
            avaiable = [e for e in elements if e not in used_elements]
            if not avaiable: break
            
            tamanho = random.randint(1, max(1, n // 4))
            k = min(tamanho, len(avaiable))
            subset = random.sample(avaiable, k=k)
            
            used_elements.update(subset)
            subsets.append(sorted(subset))

        num_random_to_add = n - len(subsets)
        for _ in range(num_random_to_add):
            tamanho = random.randint(1, n)
            subset = sorted(random.sample(elements, k=tamanho))
            subsets.append(subset)
            
        return subsets
    
    def _generate_sparse_subsets(self, n, elements):
        # *Pattern 4: Generates subsets with low density of elements.
        subsets = []
        used_elements = set()
        max_size = max(1, int(n * 0.2)) # subsets have a max of 20% of the elements
        for _ in range(n):
            tamanho = random.randint(1, max_size)
            subset = sorted(random.sample(elements, k=tamanho))
            used_elements.update(subset)
            subsets.append(subset)
        elements_set = set(elements)
        avaiable = elements_set-used_elements
        if avaiable:
            for element in avaiable:
                subsets[random.randint(0, n-1)].append(element)
        return subsets

    def _generate_dense_subsets(self, n, elements):
        # *Pattern 5: Generates subsets with high density of elements.
        subsets = []
        used_elements = set()
        min_size = max(1, int(n * 0.8)) # subsets have a max of 80% of the elements
        for _ in range(n):
            tamanho = random.randint(min_size, n)
            subset = sorted(random.sample(elements, k=tamanho))
            used_elements.update(subset)
            subsets.append(subset)

        elements_set = set(elements)
        avaiable = elements_set-used_elements
        if avaiable:
            for element in avaiable:
                subsets[random.randint(0, n-1)].append(element)
        return subsets

    def generate_instance(self, n, pattern, min_val_A=-5, max_val_A=5):
        elements = list(range(1, n + 1))
        if pattern == 'random':
            subsets = self._generate_random_subsets(n, elements)
        elif pattern == 'disjoint_groups':
            subsets = self._generate_disjoint_groups_subsets(n, elements)
        elif pattern == 'sparse':
            subsets = self._generate_sparse_subsets(n, elements)
        elif pattern == 'dense':
            subsets = self._generate_dense_subsets(n, elements)
        else:
            return None
        
        matriz_A = np.random.randint(min_val_A, max_val_A + 1, size=(n, n))
        return n, subsets, matriz_A