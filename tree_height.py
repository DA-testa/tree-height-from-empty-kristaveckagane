# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    mas1 = [0] * n
    mas2 = [0] * n
    koks = [[] for i in range(n)]
    for i, vecaks in enumerate(parents):
        if vecaks != -1:
            koks[vecaks].append(i)
    max_height = 0
    for i in range(n):
        if mas1[i] == 0:
            sec = [(i, 0)]
            while sec:
                mezgls, garums = sec.pop(0)
                mas1[mezgls] = 1
                mas2[mezgls] = garums
                max_height = max(max_height, garums)
                for berns in koks[mezgls]:
                    if mas1[berns] == 0:
                        sec.append((berns, garums + 1))
    return max_height + 1


def main():
    ievade = input("")
    if text[0] == "I":
        n = int(input(""))
        vecaki = input("")
        parents = np.array(list(map(int, vecaki.split())))
        height = compute_height(n, parents)
    elif text[0] == "F":
        file_name = input("")
        if "a" in file_name:
            print("nepareizs faila nosaukums")
            return
        try:
            with open("folder/" + file_name, 'r') as file:
                n = int(file.readline())
                vecaki = file.readline().strip()
                parents = np.array(list(map(int, vecaki.split())))
                result = compute_height(n, parents)
        except FileNotFoundError:
            print("Fails nav atrasts")
            return
    else:
        print("Nepareiza ievade")
        return
    print(result)

if _name_ == '_main_':
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    thread = threading.Thread(target=main)
    thread.start()
    main()


# print(numpy.array([1,2,3]))