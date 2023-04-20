import fileinput
import os

directory = 'logfiles\spinnaker\prepped_logs'

i = 100


for f in os.listdir(directory):
    serviceLog = os.path.join(directory, f)
    serviceName = f.replace('-labeled.log', '')
    with open(serviceLog, 'r') as file:
        commitnr = 0
        for line in file:
            if line[0] == "-" and line[1] == "-":
                commitnr = commitnr + 1
        print("commitnr " + serviceName + " = " + str(commitnr))
