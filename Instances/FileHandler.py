import numpy as np

class FileHandler:
    """
    Handles reading, writing, and cleaning files for MAX-SC-QBF instances.
    """

    def __init__(self, filepath):
        self.filepath = filepath

    def append_instance(self, pattern, n, subsets, matrix_A):
        """
        @params:
            n (int): The number of variables.
            subsets (list[list[int]]): A list of lists representing subsets.
            matrix_A (np.ndarray): A full (n x n) NumPy array for the matrix.
        """
        try:
            with open(self.filepath, 'a') as f:
                f.write(f"{pattern.upper()}\n")
                f.write(f"{n}\n")

                tamanhos_str = "".join([str(len(s))+" " for s in subsets])
                f.write(f"{tamanhos_str}\n")

                for s in subsets:
                    line_s = " ".join([str(elem) for elem in s])
                    f.write(f"{line_s}\n")

                for i in range(n):
                    elementos_triangulares = matrix_A[i, i:]
                    line_A = " ".join([str(val) for val in elementos_triangulares])
                    f.write(f"{line_A}\n")
                
                # Separator of the file, so its content is separated into blocks
                f.write("---\n")
            
            print(f"Instance successfully appended to '{self.filepath}'")

        except IOError as e:
            print(f"Error appending to file '{self.filepath}': {e}")

    def read_instances(self):
        all_instances = []
        try:
            with open(self.filepath, 'r') as f:
                content = f.read()

            if not content:
                return []

            # The file separator is ---, used to split the content into blocks
            instance_blocks = content.strip().split('---')

            for block in instance_blocks:
                block = block.strip()
                if not block:
                    continue

                lines = block.splitlines()
                line_iterator = iter(lines)

                pattern = next(line_iterator)
                n = int(next(line_iterator))
                sizes = next(line_iterator) # just to consume the line, as subset size is not used rn
                
                subsets = []
                for _ in range(n):
                    subsets.append([int(x) for x in next(line_iterator).split()])
                
                matrix_A = np.zeros((n, n), dtype=int)
                for i in range(n):
                    valores = [int(x) for x in next(line_iterator).split()]
                    for j, valor in enumerate(valores):
                        matrix_A[i, i + j] = valor
                
                all_instances.append({
                    "pattern": pattern,
                    'n': n,
                    'subsets': subsets,
                    'matrix_A': matrix_A
                })

        except (IOError, ValueError, StopIteration) as e:
            return []
        return all_instances

    def clean_file(self):
        try:
            open(self.filepath, 'w').close()
        except IOError as e:
            print(f"Error cleaning file '{self.filepath}': {e}")
