from Instances.FileHandler import FileHandler
from Instances.MAXSCQBFGenerator import MAXSCQBFGenerator
import os
import numpy as np
import random

def main():
    file = os.path.join(os.getcwd(), "instances.txt")
    fh = FileHandler(filepath=file)
    gen = MAXSCQBFGenerator()

    fh.clean_file()
    

    patterns = [
        'random',
        'sparse',
        'dense'
    ]
    n_values = [25, 50, 100, 200, 400] # n will be one of these values

    fh.clean_file()

    num_instances_to_generate = 15
    
    print(f"\n--- Generating and appending {num_instances_to_generate} instances ---")
    for i in range(num_instances_to_generate):
        print(f"Generating instance {i+1}/{num_instances_to_generate}...")
        n, subsets, matrix = gen.generate_instance(n=n_values[random.randint(0, 4)], pattern=patterns[random.randint(0, 2)])
        fh.append_instance(n, subsets, matrix)
    
    
    print("\n--- Reading all instances from the file ---")
    instances = fh.read_instances()

    if instances:
        for i, instance_data in enumerate(instances):
            print(f"\n--- Instance {i+1} Data ---")
            print(f"n: {instance_data['n']}")
            print("Subsets:")
            for s_idx, s in enumerate(instance_data['subsets']):
                print(f"  S{s_idx+1}: {s}")
            print("Matrix A:")
            print(instance_data['matrix_A'])
            print("-" * 25)
main()
