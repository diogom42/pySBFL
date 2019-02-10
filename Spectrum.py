import csv
import math
import sys
import re

from pathlib import Path

import gc


class Spectrum:
    def __init__(self, programDir, program, ver):
        self.readCovMat(programDir, program, ver)

        self.tests = len(self.pTests) + len(self.nTests)

        self.lines = 0
        if len(self.pTests) != 0: self.lines = len(self.pTests[0])
        if self.lines == 0 and len(self.nTests) != 0:
            self.lines = len(self.nTests[0])

        self.ep = self.EPs()
        self.ef = self.EFs()
        self.np = self.NPs()
        self.nf = self.NFs()

        self.metrics = list()
        for i in range(41):
            metrics = self.calcMetrics(i + 1)
            #  Normalize metrics:
            metricsMin = min(metrics)
            metricsRange = max(metrics) - min(metrics)
            if (metricsRange == 0):
                print('all suspiciousness values are equal in H' + str(i+1) + ' of V ' + str(ver))
                metricsNorm = [0 for number in metrics]
                print(metricsNorm)
            else:
                metricsNorm = [(number - metricsMin) / metricsRange for number in metrics]
            self.metrics.append(metricsNorm)

    # def readTrace(self, file):
    #     f = open(file, 'r')
    #     l = list()  # l = []
    #     for line in f:
    #         if line[0:3] == 'DA:':
    #             if int(line.split(',')[1]) == 0:
    #                 l.append(0)
    #             else:
    #                 l.append(1)
    #     f.closed
    #     return l

    def readCovMat(self, programDir, program, ver):
        self.nTests = list()
        self.pTests = list()

        matrixFile = open(programDir + program + '/' + str(ver) + '/matrix', 'r')
        CovMat = list(csv.reader(matrixFile, delimiter=','))  # append all lines as a list
        matrixFile.close()

        for j in range(len(CovMat)):  # iterate over number of tests
            if CovMat[j][-1] == '-':
                del CovMat[j][-1]
                self.nTests.append(list(map(int, CovMat[j])))
            else:
                del CovMat[j][-1]
                self.pTests.append(list(map(int, CovMat[j])))

        CovMat.clear()
        gc.collect()

    def EPs(self):
        ep = list()
        for i in range(self.lines):
            ep.append(self.epRuns(i))
        return ep

    def epRuns(self, line):
        ep = 0
        for i in self.pTests:
            if i[line] == 1:
                ep += 1
        return ep

    def EFs(self):
        ef = list()
        for i in range(self.lines):
            ef.append(self.efRuns(i))
        return ef

    def efRuns(self, line):
        ef = 0
        for i in self.nTests:
            if i[line] == 1:
                ef += 1
        return ef

    def NPs(self):
        np = list()
        for i in range(self.lines):
            np.append(self.npRuns(i))
        return np

    def npRuns(self, line):
        np = 0
        for i in self.pTests:
            if i[line] == 0:
                np += 1
        return np

    def NFs(self):
        nf = list()
        for i in range(self.lines):
            nf.append(self.nfRuns(i))
        return nf

    def nfRuns(self, line):
        nf = 0
        for i in self.nTests:
            if i[line] == 0:
                nf += 1
        return nf

    def calcMetrics(self, M):
        if M == 1:
            return self.m1()
        elif M == 2:
            return self.m2()
        elif M == 3:
            return self.m3()
        elif M == 4:
            return self.m4()
        elif M == 5:
            return self.m5()
        elif M == 6:
            return self.m6()
        elif M == 7:
            return self.m7()
        elif M == 8:
            return self.m8()
        elif M == 9:
            return self.m9()
        elif M == 10:
            return self.m10()
        elif M == 11:
            return self.m11()
        elif M == 12:
            return self.m12()
        elif M == 13:
            return self.m13()
        elif M == 14:
            return self.m14()
        elif M == 15:
            return self.m15()
        elif M == 16:
            return self.m16()
        elif M == 17:
            return self.m17()
        elif M == 18:
            return self.m18()
        elif M == 19:
            return self.m19()
        elif M == 20:
            return self.m20()
        elif M == 21:
            return self.m21()
        elif M == 22:
            return self.m22()
        elif M == 23:
            return self.m23()
        elif M == 24:
            return self.m24()
        elif M == 25:
            return self.m25()
        elif M == 26:
            return self.m26()
        elif M == 27:
            return self.m27()
        elif M == 28:
            return self.m28()
        elif M == 29:
            return self.m29()
        elif M == 30:
            return self.m30()
        elif M == 31:
            return self.m31()
        elif M == 32:
            return self.m32()
        elif M == 33:
            return self.m33()
        elif M == 34:
            return self.m34()
        elif M == 35:
            return self.m35()
        elif M == 36:
            return self.m36()
        elif M == 37:
            return self.m37()
        elif M == 38:
            return self.m38()
        elif M == 39:
            return self.m39()
        elif M == 40:
            return self.m40()
        elif M == 41:
            return self.m41()
        else:
            return list()

    def m1(self):  # Braun - Banquet
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NF = self.nf[line]
            metric.append(EF / sys.float_info.min if max(EF + EP, EF + NF) == 0 else max(EF + EP, EF + NF))
        return metric

    def m2(self):  # Dennis
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append(((EF * NP) - (EP * NF)) / (
                sys.float_info.min if (math.sqrt(self.tests * (EF + EP) * (EF + NF)) == 0) else math.sqrt(
                    self.tests * (EF + EP) * (EF + NF))))
        return metric

    def m3(self):  # Mountford
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NF = self.nf[line]
            metric.append(EF / (0.5 * (
                sys.float_info.min if (((EF * EP) + (EF * NF) + (EP * NF)) == 0) else (
                        (EF * EP) + (EF * NF) + (EP * NF)))))
        return metric

    def m4(self):  # Fossum
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NF = self.nf[line]
            metric.append(0 if (((EF + EP) * (EF + NF)) == 0) else (
                    self.tests * math.pow(EF - 0.5, 2) / ((EF + EP) * (EF + NF))))
        return metric

    def m5(self):  # Pearson
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append(self.tests * math.pow((EF * NP) - (EP * NF), 2) / (
                sys.float_info.min if ((EP + EF) * (NF + NP) * (EP + NP) * (NF + EF) == 0) else ((EP + EF) * (
                        NF + NP) * (EP + NP) * (NF + EF))))
        return metric

    def m6(self):  # Gower
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append(0 if ((EP + EF) == 0 or (NF + NP) == 0 or (NF + EF) == 0) else (1 if (EP + NP) == 0 else
                                ((EP + NP) / math.sqrt((NF + EF) * (EP + EF) * (NF + NP) * (EP + NP)))))
        return metric

    def m7(self):  # Michael
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append(4 * ((EF * NP) - (EP * NF)) / (
            sys.float_info.min if ((math.pow(EF + NP, 2) + math.pow(EP + NF, 2)) == 0) else (
                    math.pow(EF + NP, 2) + math.pow(EP + NF, 2))))
        return metric

    def m8(self):  # Pierce
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append(0 if (EF == 0 and NP == 0) else (((EF * NF) + (NF * EP)) / (
                sys.float_info.min if (((EF * NF) + (2 * (NF * NP)) + (EP * NP)) == 0) else (
                        (EF * NF) + (2 * (NF * NP)) + (EP * NP)))))
        return metric

    def m9(self):  # Baroni-Urbani & Buser
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append((math.sqrt(EF * NP) + EF) / (sys.float_info.min if (
                    (math.sqrt(EF * NP) + EF + EP + NF) == 0) else (math.sqrt(EF * NP) + EF + EP + NF)))

        return metric

    def m10(self):  # Tarwid
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NF = self.nf[line]
            metric.append(((self.tests * EF) - ((NF + EF) * (EF + EP))) / (sys.float_info.min if ((self.tests * EF) + (
                            (NF + EF) * (EF + EP)) == 0) else (self.tests * EF) + ((NF + EF) * (EF + EP))))
        return metric

    def m11(self):  # Ample
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append(abs((EF / (sys.float_info.min if ((EF + NF) == 0) else (EF + NF))) -
                              (EP / (sys.float_info.min if ((EP + NP) == 0) else (EP + NP)))))

        return metric

    def m12(self):  # Phi (Geometric Mean)
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append(((EF * NP) - (NF * EP)) / (sys.float_info.min if (math.sqrt((EF + EP) * (EF + NF) *
                        (EP + NP) * (NF + NP)) == 0) else math.sqrt((EF + EP) * (EF + NF) * (EP + NP) * (NF + NP))))
        return metric

    def m13(self):  # Arithmetic Mean
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append((2 * ((EF * NP) - (NF * EP))) /
                          (sys.float_info.min if (((EF + EP) * (NP + NF) + (EF + NF) * (EP + NP)) == 0)
                        else ((EF + EP) * (NP + NF) + (EF + NF) * (EP + NP))))

        return metric

    def m14(self):  # Cohen
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append((2 * ((EF * NP) - (NF * EP))) /
                          (sys.float_info.min if (((EF + EP) * (NP + EP) + (EF + NF) * (NF + NP)) == 0)
                          else ((EF + EP) * (NP + EP) + (EF + NF) * (NF + NP))))

        return metric

    def m15(self):  # Fleiss
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append((4 * ((EF * NP) - (NF * EP)) - math.pow(NF - EP, 2)) /
                          (sys.float_info.min if (((2 * EF + NF + EP) + (2 * NP + NF + EP)) == 0)
                          else ((2 * EF + NF + EP) + (2 * NP + NF + EP))))

        return metric

    def m16(self):  # Zoltar
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NF = self.nf[line]
            metric.append(EF / (sys.float_info.min if ((EF + NF + EP + (
                    10000 * NF * EP / (sys.float_info.min if (EF == 0) else EF))) == 0)
                    else (EF + NF + EP + (10000 * NF * EP / (sys.float_info.min if (EF == 0) else EF)))))

        return metric

    def m17(self):  # Harmonic Mean
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append((((EF * NP) - (NF * EP)) * ((EF + EP) * (NP + NF) + (EF + NF) * (EP + NP))) /
                          (sys.float_info.min if ((EF + EP) * (NP + NF) * (EF + NF) * (EP + NP) == 0)
                          else (EF + EP) * (NP + NF) * (EF + NF) * (EP + NP)))

        return metric

    def m18(self):  # Rogot2
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append(0.25 * ((EF / (sys.float_info.min if ((EF + EP) == 0) else (EF + EP))) +
                                  (EF / (sys.float_info.min if ((EF + NF) == 0) else (EF + NF))) +
                                  (NP / (sys.float_info.min if ((NP + EP) == 0) else (NP + EP))) +
                                  (NP / (sys.float_info.min if ((NP + NF) == 0) else (NP + NF)))))
        return metric

    def m19(self):  # Simple Matching
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append((EF + NP) / (sys.float_info.min if ((EF + EP + NP + NF) == 0) else (EF + EP + NP + NF)))

        return metric

    def m20(self):  # Rogers & Tanimoto
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append((EF + NP) /
                          (sys.float_info.min if ((EF + NP + 2 * (NF + EP)) == 0) else (EF + NP + 2 * (NF + EP))))

        return metric

    def m21(self):  # Hamming
        metric = list()
        for line in range(self.lines):
            EF = self.ef[line]
            NP = self.np[line]
            metric.append(EF + NP)

        return metric

    def m22(self):  # Mamann
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append((EF + NP - NF - EP) /
                          (sys.float_info.min if ((EF + NF + EP + NP) == 0) else (EF + NF + EP + NP)))

        return metric

    def m23(self):  # Sokal
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append(2 * (EF + NP) /
                          (sys.float_info.min if ((2 * (EF + NP) + NF + EP) == 0) else (2 * (EF + NP) + NF + EP)))

        return metric

    def m24(self):  # Scott
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append(4 * (EF * NP - NF * EP) - math.pow(NF - EP, 2) /
                          (sys.float_info.min if (((2 * EF + NF + EP) * (2 * NP + NF + EP)) == 0)
                          else ((2 * EF + NF + EP) * (2 * NP + NF + EP))))

        return metric

    def m25(self):  # Rogot1
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append(0.5 * ((EF / (sys.float_info.min if ((2 * EF + NF + EP) == 0) else (2 * EF + NF + EP))) +
                                 (NP / (sys.float_info.min if ((2 * NP + NF + EP) == 0) else (2 * NP + NF + EP)))))

        return metric

    def m26(self):  # Kulczynski
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NF = self.nf[line]
            metric.append(EF / (1 if ((NF + EP) == 0) else (NF + EP)))

        return metric

    def m27(self):  # Anderberg
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NF = self.nf[line]
            metric.append(EF / (sys.float_info.min if ((EF + 2 * (NF + EP)) == 0) else (EF + 2 * (NF + EP))))

        return metric

    def m28(self):  # Dice
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NF = self.nf[line]
            metric.append(2 * EF / (sys.float_info.min if ((EF + NF + EP) == 0) else (EF + NF + EP)))

        return metric

    def m29(self):  # Goodman
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NF = self.nf[line]
            metric.append(2 * EF - NF - EP / (sys.float_info.min if ((2 * EF + NF + EP) == 0) else (2 * EF + NF + EP)))

        return metric

    def m30(self):  # Jaccard
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append(EF / (sys.float_info.min if ((EF + NF + EP) == 0) else (EF + NF + EP)))

        return metric

    def m31(self):  # Sorense-Dice
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NF = self.nf[line]
            metric.append(2 * EF / (sys.float_info.min if ((2 * EF + NF + EP) == 0) else (2 * EF + NF + EP)))

        return metric

    def m32(self):  # Tarantula
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append(0 if (NF + EF) == 0 else 1 if (EP + NP) == 0 else ((EF / (NF + EF)) /
                          (sys.float_info.min if (((EP / (EP + NP)) + (EF / (NF + EF))) == 0)
                          else ((EP / (EP + NP)) + (EF / (NF + EF))))))

        return metric

    def m33(self):  # Ochiai
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NF = self.nf[line]
            metric.append(0 if (NF + EF) == 0 else (EF / math.sqrt((NF + EF) * ((sys.float_info.min if (EF == 0) else EF) +
                                                      (sys.float_info.min if (EP == 0) else EP)))))

        return metric

    def m34(self):  # Ochiai2
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append(EF * NP / (sys.float_info.min if ((math.sqrt((EF + EP) * (NP + NF) * (EF + NF) *
                                (EP + NP))) == 0) else (math.sqrt((EF + EP) * (NP + NF) * (EF + NF) * (EP + NP)))))

        return metric

    def m35(self):  # OP2
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            metric.append(EF - EP / (EP + NP + 1))
        return metric

    def m36(self):  # Barinel
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            metric.append(0 if ((EP + EF) == 0) else 1 - EP / (EP + EF))
        return metric

    def m37(self):  # DStar
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NF = self.nf[line]
            metric.append(2 * EF / (1 if ((EP + NF) == 0) else (EP + NF)))
        return metric

    def m38(self):  # GP02
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            metric.append(2 * (EF * math.sqrt(NP)) +math.sqrt(EP))
        return metric

    def m39(self):  # GP03
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            metric.append(math.sqrt(abs(math.pow(EF, 2)-math.sqrt(EP))))
        return metric

    def m40(self):  # GP13
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            metric.append(EF * (1 + 1 / (sys.float_info.min if ((EP + EF) == 0) else (2 * EP + EF))))
        return metric

    def m41(self):  # GP19
        metric = list()
        for line in range(self.lines):
            EP = self.ep[line]
            EF = self.ef[line]
            NP = self.np[line]
            NF = self.nf[line]
            metric.append(EF * math.sqrt(abs(EP - EF + NF - NP)))
        return metric
