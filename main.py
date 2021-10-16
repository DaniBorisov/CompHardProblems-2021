import Decoder


def print_hi(name):

    content = Decoder.getInput()
    decoder = Decoder.Decoder()
    decoder.decode(content)
    print(decoder.get_k())
    print(decoder.get_s())
    print(decoder.get_list_t())
    print(decoder.get_list_R())




if __name__ == '__main__':
    print_hi('PyCharm')
