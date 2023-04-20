import fileinput
import os

# reads minus bots logs and outputs the labeled services

read_directory = 'logfiles\spinnaker\minus_bots'
write_directory = 'logfiles\spinnaker\prepped_logs'


for f in os.listdir(read_directory):
    serviceLog = os.path.join(read_directory, f)
    serviceName = f.replace('minus_bots.log', '')
    with open(serviceLog, 'r', errors='ignore') as file:
        data = file.readlines()
        counter = 0
        for line in data:
            if not (line[0] == '-' or line == '\n'):
                for i in range(3, len(line)):
                    if(line[i] == '\t'):
                        new_line = line[0:i+1] + serviceName + "\n"
                        data[counter] = new_line
            counter = counter + 1

    with open(write_directory + "/" + serviceName + '-labeled.log', 'w') as new_file:
        new_file.writelines(data)
