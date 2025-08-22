class ReportLogger:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def write_instance(self, instance_idx, total):
        try:
            with open(self.filepath, 'a') as f:
                f.write(f"INSTANCE {instance_idx}/{total}\n")
        except IOError as e:
            print(f"Error adding instance index to file '{self.filepath}': {e}")


    def append_result(self, pattern, n, solution_val , gap, execution_time):
        try:
            with open(self.filepath, 'a') as f:
                f.write(f"[SIZE] {n} [PATTERN] {pattern.upper()} \n")
                f.write(f"[SOLUTION VALUE] {solution_val}\n")
                f.write(f"[GAP] {gap}\n")
                f.write(f"[EXECUTION TIME] {execution_time}\n")
                f.write("---\n")
        except IOError as e:
            print(f"Error appending to file '{self.filepath}': {e}")

    def clean_file(self):
        try:
            open(self.filepath, 'w').close()
        except IOError as e:
            print(f"Error cleaning file '{self.filepath}': {e}")