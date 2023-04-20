import fileinput

data = []
counter = 0


def addCommit(commitDate):
    data.append(commitDate + "\n")


with open("logfiles/metadata/refactor 1/pre_refactor1.log", 'r') as file:
    numberedLines = file.readlines()
    for line in numberedLines:
        if line[0] == '-' and counter + 1 < len(numberedLines) and numberedLines[counter + 1] != "\n":
            addCommit(line[11:21])
        counter = counter + 1
    with open('logfiles/metadata/refactor 1/pre_refactor1-commitdates.log', 'w') as file:
        file.writelines(data)
