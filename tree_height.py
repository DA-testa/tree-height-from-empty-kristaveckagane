import sys
import threading
import numpy


def compute_height(n, parents):
    koks = [[]for i in range(n)]
    for i, vecaks in enumerate(parents):
        if vecaks != -1:
            koks[vecaks].append(i)
    max_height = 0
    for i in range(n):
        mas1 = [0] * n
        mas2 = [0] * n
        if mas1[i] == 0:
            sec = [(i, 0)]
        while sec:
            mezgls, garums = sec.pop()
            mas1[mezgls] = 1
            mas2[mezgls] = garums
            max_height = max(max_height, garums)
            for berns in koks[mezgls]:
                if mas1[berns] == 0:
                    sec.append((berns, garums + 1))
    return max_height + 1

def main():
    ievade = input("").strip()
    if "i" == ievade.lower() :
        n = int(input("").strip())
        vecaki = input("").strip().split()
        parents = [int(x) for x in vecaki]
        result = compute_height(n, parents)
        print(result)
    elif "f" == ievade.lower() :
        file = input("").strip()
        if "a" in file.lower():
            print("Nepareiza faila nosaukums. Faila nosaukumā nedrīkst būt burts 'a'.")
            return
        with open(file, "r") as f:
            n = int(f.readline().strip())
            vecaki = f.readline().strip().split()
            parents = [int(x) for x in vecaki]
            result = compute_height(n, parents)
            print(result)
    else:
        print("nepareizi")

if __name__ == '_main_':
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    thread = threading.Thread(target=main)
    thread.start()
main()