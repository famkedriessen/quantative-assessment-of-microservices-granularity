import fileinput
import os

directory = 'logfiles\spinnaker\prepped_logs'


for f in os.listdir(directory):
    serviceLog = os.path.join(directory, f)
    serviceName = f.replace('-labeled.log', '')
    with open(serviceLog, 'r') as file:
        churn = 0
        for line in file:
            if serviceName in line:
                churn = churn + 1
        print("churn " + serviceName + " = " + str(churn))
