import fileinput


counter = 0


def namesService1(line):
    return "ref-impl" in line


def namesService2(line):
    return "core/" in line


with open("logfiles/metadata/refactor 1/pre/pre_refactor1.log", 'r') as file:
    data = file.readlines()
    for line in data:
        if namesService1(line):
            newline = "\t".join(line.split(
                "\t")[:2]) + '\tref-impl\n'
            data[counter] = newline
        elif namesService2(line):
            newline = "\t".join(line.split(
                "\t")[:2]) + '\tcore\n'
            data[counter] = newline
        else:
            if not (line[0] == '-' or line == '\n'):
                data[counter] = 'ignore\n'
        counter = counter + 1
    with open('logfiles/metadata/refactor 1/pre/labeledservices_ref-impl_core.log', 'w') as new_file:
        for line in data:
            if not line == 'ignore\n':
                new_file.write(line)
