# Obtain reflexive, symmetric and transitive relations from a given set of numbers.


def reflexive(numbers):
    print("REFLEXIVE = [{", end="\n  ")
    for i in numbers:
        for j in numbers:
            if i == j:
                print("(" + str(i) + "," + str(j) + ")", end="\n  ")
    print("}]")


def symmetric(numbers):
    print("SYMMETRIC = [", end="\n")
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            print("  {", end=" ")
            print("(" + str(numbers[i]) + "," + str(numbers[j]) + ")", end=" ")
            print("(" + str(numbers[j]) + "," + str(numbers[i]) + ")", end=" ")
            print("}")
    print("]")


def transitive(numbers):
    print("TRANSITIVE = [", end="\n")
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                print("  {", end=" ")
                print("(" + str(numbers[i]) + "," + str(numbers[j]) + ")", end=" ")
                print("(" + str(numbers[j]) + "," + str(numbers[k]) + ")", end=" ")
                print("(" + str(numbers[i]) + "," + str(numbers[k]) + ")", end=" ")
                print("}")
    print("]")


if __name__ == "__main__":
    n = int(input("How many elements in the set?\n> "))
    numbers = []
    print("Enter numbers : ")
    for i in range(n):
        x = int(input("> "))
        numbers.append(x)

    numbers_set = set(numbers)
    numbers_set = list(numbers_set)
    reflexive(numbers_set)
    symmetric(numbers_set)
    transitive(numbers_set)
