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

        if not self.k.isdecimal():
            sys.exit("NO!")

        if not self.s.islower():
            sys.exit("NO!")

        offset = 2

        for i in range(0, int(self.k)):
            if not self.STinput[i + offset].isalpha():
                sys.exit("NO!")
            else:
                self.listT.append(STinput[i + offset])

        for i in range(offset + int(self.k), len(STinput)):
            # prog = re.compile("(^[A-Z]: )" + "(([a-z])*, )*")
            Upp = re.compile("^[A-Z]:")
            # if not Upp.match(self.STinput[i]):
            #     print("First letter")
            #     sys.exit("NO!")
            # low = re.compile("^[a-z]+, ")
            #
            # a, b = map(list, Upp.split(self.STinput[i]))
            # # splitted = Upp.split(self.STinput[i])
            # print(a)
            # print(b)
            # print(len(b))
            # for j in range(0, len(b)):
            #     print(b[j])
            #     if not low.match(b[j]):
            #         print("lower case ")
            #         sys.exit("NO!")
            #
            # self.listR.append(STinput[i])
                    # if not re.match("^[A-Z]: " + "(([a-z]*), )+", self.STinput[i]):
            if not Upp.match(self.STinput[i]):
                print("matching")
                sys.exit("NO!")
            else:
                self.listR.append(STinput[i])

    def get_k(self):
        return self.k

    def get_s(self):
        return self.s

    def get_list_t(self):
        return self.listT

    def get_list_R(self):
        return self.listR
