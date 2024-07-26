import matplotlib.pyplot as plt

def collatzseq(num):
    interac = 0
    while num != 1:
        if num%2 == 0:
            interac += 1
            num /= 2
        else:
            interac += 1
            num = 3 * num + 1
    return interac

def collatzespec(num):
    if num%2 == 0:
        num /= 2
        return num
    else:
        num = 3 * num + 1
        return num
    

def main():
    print("This is a Collatz's Conjecture tester")
    op = 2
    while op != 0 and op != 1:
        print("Enter 0 to graph the number of interactions from 1 to N. Enter 1 to get the number of interactions of number the N and its results graph")
        op = int(input())
        if op == 0:
            seq()
        elif op == 1:
            espec()
        else:
            print(op, "is not a valid entry")

def seq():
    print("Enter a integer greater than 0 to calculate. To enter 0 or lower ends the program")
    num = int(input())
    while num > 0:
        x = []
        y = []
        for i in range(num):
            x.append(i+1)
            yp = collatzseq(i+1)
            y.append(yp)
        plt.plot(x,y)
        plt.show()
        print("Enter a integer greater than 0 to calculate. To enter 0 or lower ends the program")
        num = int(input())

def espec():
    print("Enter a integer greater than 0 to calculate. To enter 0 or lower ends the program")
    num = int(input())
    while num > 0:
        y = []
        y.append(num)
        interac = 1
        while num > 1:
            num = collatzespec(num)
            interac += 1
            y.append(num)
            print(int(num))
        if interac == 1:
            y.append(1)
        x = [i+1 for i in range(interac)]
        plt.yscale("log")
        plt.plot(x,y)
        print("The number of interactions was", interac-1)
        plt.show()
        print("Enter a integer greater than 0 to calculate. 0 or lower ends the program")
        num = int(input())

main()
