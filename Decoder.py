import re
import sys


def getInput():
    inputList = []
    for line in sys.stdin:
        inputList.append(line.rstrip())

    return inputList


class Decoder:
    def __init__(self):
        self.k = 0
        self.s = None
        self.listT = []
        self.listR = []

    def decode(self, STinput):
        self.STinput = STinput
        self.k = STinput[0]
        self.s = STinput[1]
        offset = 2

        if not self.k.isdecimal():
            return False

        if not self.s.islower():
            return False

        for i in range(0, int(self.k)):
            if not self.STinput[i + offset].isalpha():
                return False
            else:
                self.listT.append(STinput[i + offset])

        for i in range(offset + int(self.k), len(STinput)):
            Upp = re.compile("^[A-Z]:")
            low = re.compile("[a-z]")

            if not Upp.match(self.STinput[i]):
                print("First letter")
                return False

            a, b = map(list, Upp.split(self.STinput[i]))
            for j in range(0, len(b)):
                if b[j].isalpha():
                    if not low.match(b[j]):
                        return False

            self.listR.append(STinput[i])

        return True

    def get_k(self):
        return self.k

    def get_s(self):
        return self.s

    def get_list_t(self):
        return self.listT

    def get_list_R(self):
        return self.listR
