from Spectrum import Spectrum
import csv

def susp(prog, ver, H):
    try:
        spect = Spectrum("", prog, ver)

        susp = list()

        # abre um novo arquivo de trace
        with open(prog + '/' + ver + '/app_base.info', 'r') as trace:
            lines = trace.read().splitlines()
            for line in lines:
                line = line.replace(':', ',').split(',')
                if line[0] == 'DA':
                    susp.append(list())
                    susp[-1].append(int(line[1]))
                    for h in H:
                        susp[-1].append(spect.metrics[h][len(susp)-1])

        return susp
    except ValueError:
        return list()
    except IndexError:
        return list()

if __name__ == "__main__":
    progList = open('problems', 'r').read().splitlines()

    for prog in progList:
        print(prog)
        verList = open(prog + '/versions', 'r').read().splitlines()

        for ver in verList:
            print(ver)
            if ver != 'fix':
                with open(prog + '/' + str(ver) + '/susp', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerows(susp(prog, ver, [31, 32, 34, 36, 29, 10]))# Tarantula, Ochiai, OP2, DStar, Jaccard, Ample