def x(sentence, next_coroutine):
    words = sentence.split(" ")
    for temp in words:
        next_coroutine.send(temp)
    next_coroutine.close()


def u(next_coroutine=None):
    pattern = input("Enter the pattern you are searching for : ")
    print("Searching String {}".format(pattern))
    try:
        while True:
            temp = yield
            if pattern in temp:
                next_coroutine.send(temp)
            else:
                print("Match not found")
    except GeneratorExit:
        print("Completed Matching Process")


def printing():
    try:
        while True:
            temp = yield
            print(temp + " is present in the string")
    except GeneratorExit:
        print("Completed Pipelining")


d = printing()
d.__next__()
f = u(next_coroutine=d)
f.__next__()


sentence = input("Enter the sentence : ")
x(sentence, f)

input("Press Enter key to exit ")
