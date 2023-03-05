# python3
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
    if "i" in ievade.lower():
        n = int(input(""))
        vecaki=input("")
        parents = numpy.array(list(map(int,vecaki.split())))
        result=compute_height(n, parents)
        print(result)
    elif "f" in ievade.lower():
        file = input("")
        if "a" in file.lower():
            print("Nepareiza faila nosaukums. Faila nosaukumā nedrīkst būt burts 'a'.")
            return
        with open(file, "r") as f:
            n = int(f.readline())
            vecaki = f.readline().strip()
            parents = numpy.array(list(map(int,vecaki.split())))
            result=compute_height(n, parents)
            print(result)
        f.close()
    else:
        print("nepareizi")

main()







    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.



# print(numpy.array([1,2,3]))