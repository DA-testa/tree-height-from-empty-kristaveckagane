# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    koks = [[]for i in range(n)]
    for i, vecaks in enumerate(parents):
        if parent != -1;
          koks[vecaks].append(i)
    max_height=0
    for i in range(n):
        if mas1[i]==0:
            sec = [(i, 0)]
        while sec:
            node, height = sec.pop(0)
            mas1[node]=1
            mas2[node]=height
            max_height = max(max_height, height)
            for berns in koks[node]:
                if mas1[berns]==0
                sec.append((berns, height + 1))
    # Your code here
    return max_height + 1
    mas1 = [0]* n
    mas2=[0]* n


def main():
    # implement input form keyboard and from files
     ievade = input("")
    if "i" in ievade.lower():
        n = int(input())
        vecaki=input()
        parents = numpy.array(list(map(int,vecaki.split())))
        result=compute_height(n, parents)
        print(result)
    elif "f" in ievade.lower():
        file = input("")
        if file[0] != "a":
        with open(file, "r") as f:
            n = int(file.readline())
            vecaki = f.readline().strip()
            parents = numpy.array(list(map(int,vecaki.split())))
            result=compute_height(n, parents)
            print(result)
            else:
            print("nepareiza faila nosaukums")
            return

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))