import fileinput
import os

directory = 'logfiles\spinnaker\logfiles'
botCommit = False

counter = 0

for f in os.listdir(directory):
    if f.endswith(".log"):
        serviceLog = os.path.join(directory, f)
        serviceName = f.replace('.log', '')
        if serviceName == "orca":
            a = 1
        with open(serviceLog, 'r', errors='ignore') as file:
            data = file.readlines()
            for i in range(0, len(data)):
                line = data[i]
                if line[0] == "-" and line[1] == "-" and "bot" in line:
                    botCommit = True
                    data[i] = 'ignore\n'
                    while botCommit:
                        i = i + 1
                        nextLine = data[i]
                        if nextLine[0] == "-" and nextLine[1] == "-" and not "bot" in nextLine:
                            botCommit = False
                        else:
                            data[i] = 'ignore\n'
            with open("logfiles/spinnaker/minus_bots/" + serviceName + 'minus_bots.log', 'w') as new_file:
                for line in data:
                    if not line == 'ignore\n':
                        new_file.write(line)
