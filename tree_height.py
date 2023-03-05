# python3

import sys
import threading
import numpy


def compute_height(n, parents):
     koks = [[]for i in range(n)]
    for i, vecaks in enumerate(parents):
        if vecaks != -1:
            koks[vecaks].append(i)
    max_height=0
    for i in range(n):
        mas1 = [0]* n
        if mas1[i]==0:
            sec = [(i, 0)]
        while sec:
            mezgls, garums = sec.pop(0)
            mas1[mezgls]=1
            max_height = max(max_height, garums)
            for berns in koks[mezgls]:
                if mas1[berns]==0:
                 sec.append((berns, garums + 1))
                 mas1[berns]=1
    return max_height + 1

def main():
    ievade = input("")
    if "i" in ievade.lower():
        n = int(input(""))
        vecaki = input("").strip().split()
        parents = [int(i) for i in vecaki]
        result = compute_height(n, parents)
        print(result)
    elif "f" in ievade.lower():
        file = input("")
        if "a" in file.lower():
            print("Nepareiza faila nosaukums. Faila nosaukumā nedrīkst būt burts 'a'.")
            return
        try:
            with open(file, "r") as f:
                n = int(f.readline())
                vecaki = f.readline().strip().split()
                parents = [int(i) for i in vecaki]
                result = compute_height(n, parents)
                print(result)
        except FileNotFoundError:
            print("fails nav atrasts")
            return
    else:
        print("nepareizi")


if __name__ == "__main__":
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()
    main()

# print(numpy.array([1,2,3]))