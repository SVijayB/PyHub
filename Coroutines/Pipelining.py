def x(sentence, next_coroutine):
    words = sentence.split(" ")
    for temp in words:
        next_coroutine.send(temp)
    next_coroutine.close()

def u(pattern = "Hello", next_coroutine=None):
    print("Searching String {}".format(pattern))
    try:
        while True:
            temp = (yield)
            if pattern in temp:
                next_coroutine.send(temp)
    except GeneratorExit:
        print("Completed Matching Process")

def printing():
    try:
        while True:
            temp = (yield)
            print(temp)
    except GeneratorExit:
        print("Completed Pipelining")


d = printing()
d.__next__()
f = u(next_coroutine=d)
f.__next__()


sentence = "Hello there, how are you?"
x(sentence, f)