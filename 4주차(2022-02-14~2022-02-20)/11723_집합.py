import sys

data = []
for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if len(command) == 2:
        oper = command[0]
        x = int(command[1])
    else:
        oper = command[0]

    if oper == "add":
        if x not in data:
            data.append(x)
    elif oper == "remove":
        if x in data:
            data.remove(x)
    elif oper == "check":
        if x not in data:
            print(0)
        else:
            print(1)
    elif oper == "toggle":
        if x not in data:
            data.append(x)
        else:
            data.remove(x)
    elif oper == "all":
        data = [i for i in range(1, 21)]
    elif oper == "empty":
        data = []