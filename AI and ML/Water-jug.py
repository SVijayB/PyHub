def solve(jug1, jug2):
    print("%d\t%d" % (jug1, jug2))
    if jug2 is fill:
        return
    elif jug2 is max2:
        solve(0, jug1)
    elif jug1 != 0 and jug2 is 0:
        solve(0, jug1)
    elif jug1 is fill:
        solve(jug1, 0)
    elif jug1 < max1:
        solve(max1, jug2)
    elif jug1 < (max2 - jug2):
        solve(0, (jug1 + jug2))
    else:
        solve(jug1 - (max2 - jug2), (max2 - jug2) + jug2)


if __name__ == "__main__":
    max1 = int(input("Enter maximum capacity of jug1: "))
    max2 = int(input("Enter maximum capacity of jug2: "))
    fill = int(input("Enter final capacity of jug: "))
    print("JUG1\tJUG2")
    solve(0, 0)
