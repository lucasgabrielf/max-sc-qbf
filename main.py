from Instances.FileHandler import FileHandler
from Model.ReportLogger import ReportLogger
import Model.PLModel as PLModel
import os

instances_file = os.path.join(os.getcwd(), "instances.txt")
report_file = os.path.join(os.getcwd(), "report.txt")
fh = FileHandler(filepath=instances_file)
reportLogger = ReportLogger(filepath=report_file)

reportLogger.clean_file()

instances = fh.read_instances()

total_instances = len(instances)
for i, instance in enumerate(instances):
    reportLogger.write_instance(i+1, total=total_instances)
    solution_val, gap, execution_time = PLModel.create_model(instance, reportLogger)