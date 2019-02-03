import csv

def getCovMat(prog, v, testSize):
    outputs = open(prog + '/outputs.txt', 'r').read().splitlines()

    covMat = list()

    #identificva indice dos testes negativos da versao
    comp = open(prog + '/comp' + str(v), 'r').read().splitlines()
    failed = list()
    for c in comp:
        failed.append(outputs.index(c))

    #itera sobre os arquivos de traces de cada dado de teste
    for t in range(testSize):
        covMat.append(list())

        #abre um novo arquivo de trace
        with open(prog + '/' + str(v) +'/traces/trace' + str(t + 1) + '.info', 'r') as trace:
            lines = trace.read().splitlines()
            for line in lines:
                line = line.replace(':', ',').split(',')
                if line[0] == 'DA':
                    covMat[-1].append(0 if int(line[2]) == 0 else 1)
        # se for negativo append '-', senao, append '+'
        covMat[-1].append('-' if t in failed else '+')

    return covMat

def runList():
    progList = open('A', 'r').read().splitlines()

    for prog in progList:
        print(prog)
        verList = open(prog + '/versions', 'r').read().splitlines()
	numTests = len(open(prog + '/universe', 'r').read().splitlines())
    
        for ver in verList:
            matrix = getCovMat(prog, ver, numTests)
            with open(prog + '/' + str(ver) + '/matrix', 'w') as f:
                writer = csv.writer(f)
                writer.writerows(matrix)
        

runList()

#prog = '45-A'
#ver = '45-A-bug-3422457-3422477'
