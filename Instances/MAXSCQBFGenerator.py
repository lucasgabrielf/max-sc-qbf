import numpy as np
import random

class MAXSCQBFGenerator:
    """
    Generates random instances of the MAX-SC-QBF problem.
    """
    
    def _generate_random_subsets(self, n, elements):
        # *Pattern 1: Generates purely random subsets.
        subsets = []
        used_elements = set()

        for _ in range(n):
            size = random.randint(1, n)
            subset = sorted(random.sample(elements, k=size))
            used_elements.update(subset)
            subsets.append(subset)
    
        universe = set(elements)
        available = universe-used_elements
        if available:
            for element in available:
                random_idx = random.randint(0, n-1)
                subsets[random_idx].append(element)
                subsets[random_idx].sort()
        return subsets
    
    def _generate_sparse_subsets(self, n, elements):
        # *Pattern 2: Generates subsets with low density of elements.
        subsets = []
        used_elements = set()
        max_size = max(1, int(n * 0.2)) # subsets have a max of 20% of the elements

        for _ in range(n):
            size = random.randint(1, max_size)
            subset = sorted(random.sample(elements, k=size))
            used_elements.update(subset)
            subsets.append(subset)

        universe = set(elements)
        available = universe-used_elements
        if available:
            for element in available:
                random_idx = random.randint(0, n-1)
                subsets[random_idx].append(element)
                subsets[random_idx].sort()
        return subsets

    def _generate_dense_subsets(self, n, elements):
        # *Pattern 3: Generates subsets with high density of elements.
        subsets = []
        used_elements = set()
        min_size = max(1, int(n * 0.8)) # subsets have a max of 80% of the elements

        for _ in range(n):
            size = random.randint(min_size, n)
            subset = sorted(random.sample(elements, k=size))
            used_elements.update(subset)
            subsets.append(subset)

        universe = set(elements)
        available = universe-used_elements
        if available:
            for element in available:
                random_idx = random.randint(0, n-1)
                subsets[random_idx].append(element)
                subsets[random_idx].sort()
        return subsets

    def generate_instance(self, n, pattern, min_val_A=-5, max_val_A=5):
        elements = list(range(1, n + 1))
        if pattern == 'random':
            subsets = self._generate_random_subsets(n, elements)
        elif pattern == 'sparse':
            subsets = self._generate_sparse_subsets(n, elements)
        elif pattern == 'dense':
            subsets = self._generate_dense_subsets(n, elements)
        else:
            return None, None, None, None
        
        matrix_A = np.random.randint(min_val_A, max_val_A + 1, size=(n, n))
        return n, subsets, matrix_A