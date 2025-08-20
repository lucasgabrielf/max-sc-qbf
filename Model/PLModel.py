from mip import *
import time

def create_model(instance, reportLogger):
    n = instance['n']
    subsets = instance['subsets']
    matrix_A = instance['matrix_A']

    m = Model(name="MAX-SC-QBF")

    # *variables
    x = [ m.add_var(var_type=BINARY, name=f"x_{i}") for i in range(n) ]
    
    # matrix of binary variables; y_ij indicate if set i and set j are both active or not.
    y = [ [ m.add_var(var_type=BINARY, name=f"y_{i}{j}") for j in range(n) ] for i in range(n) ] 

    # *objective function
    m.objective = maximize( xsum( matrix_A[i][j]*y[i][j]  for i in range(n) for j in range(i, n)) )

    # *constraints
    for i in range(n):
        for j in range(n):
            m += y[i][j] <= x[i]
            m += y[i][j] <= x[j]
            m += y[i][j] >= x[i] + x[j] - 1

    print(subsets)
    for i in range(n):
        m += xsum( x[j] for j in range(n) if (i+1) in subsets[j] ) >= 1

    print("\nStarting optimization...")
    start_time = time.time()
    m.max_seconds = 600
    m.optimize()
    execution_time = time.time() - start_time

    # *results
    print("\n--- Results ---")
    if m.num_solutions:
        solution_val = m.objective_value
        gap = m.gap
        print(f"Solution value (Objective): {solution_val:.2f}")
        print(f"Optimality Gap: {gap*100:.2f}%")
        print(f"Execution Time: {execution_time:.4f} seconds")
        
        print("\nSolution matrix for y_ij:")
        for i in range(n):
            # Print the value of each variable in the row
            row_values = [int(y[i][j].x) for j in range(n)]
            print(row_values)
            reportLogger.append_result(solution_val, gap, execution_time)
            return solution_val, gap, execution_time
    else:
        print("No solution found.")
        return None, None, None

