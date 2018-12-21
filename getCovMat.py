def getCovMat(prog, v, testSize):
    outputs = open(prog + '/outputs.txt', 'r').read().splitlines()

    covMat = list()

    #identificva indice dos testes negativos da versao
    comp = open(prog + '/compv' + str(v), 'r').read().splitlines()
    failed = list()
    for c in comp:
        failed.append(outputs.index(c))

    #itera sobre os arquivos de traces de cada dado de teste
    for t in range(testSize):
        covMat.append(list())

        #abre um novo arquivo de trace
        with open(prog + '/v' + str(v) +'/traces/trace' + str(t + 1) + '.info', 'r') as trace:
            lines = trace.read().splitlines()
            for line in lines:
                line = line.replace(':', ',').split(',')
                if line[0] == 'DA':
                    covMat[-1].append(0 if int(line[2]) == 0 else 1)
        # se for negativo append '-', senao, append '+'
        covMat[-1].append('-' if t in failed else '+')

    print(covMat)

# versions = open(prog + '/versions', 'r').read().splitlines()
getCovMat('45-A', 2, 25)