import csv
with open('45-A/v2/traces/trace1.info', 'r') as trace:
    lines = trace.read().splitlines()
    for line in lines:
        line = line.replace(':', ',').split(',')
        if line[0] == 'DA' and int(line[2]) > 0:
            print(line[1])