import fileinput

counter = 0

with open("logfiles/graphql-config.log", 'r') as file:
    data = file.readlines()
    for line in data:

        if not (line[0] == '-' or line == '\n'):
            for i in range(3, len(line)):
                if(line[i] == '\t'):
                    new_line = line[0:i+1] + "graphql/" + line[i+1:]
                    data[counter] = new_line
        counter = counter + 1
    with open('logfiles/graphql-config-prepped.log', 'w') as new_file:
        new_file.writelines(data)
