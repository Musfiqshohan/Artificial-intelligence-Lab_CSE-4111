# https://www.cs.ubc.ca/~mack/Publications/AI77.pdf
import networkx as nx
import random

from AC_REVISE import REVISE
from Constraints import isSatisfied
from GraphConstruct import designConstraintGraph


def AC_I(G,D, C):

    queue=[]

    for e in G.edges:
        queue.append(e)



    cnt=0
    while(True):
        change = False

        # print("Iteration ",cnt)
        # cnt=cnt+1

        for edge in queue:
            Xi,Xj=edge
            d=REVISE(Xi,Xj,D,C)
            change=change or d
            d=REVISE(Xj,Xi,D,C)     # reverse order is done auto in AC-3 but not in AC-1
            change=change or d


        if(change==False):
            break
        else:
            continue

    for i in G.nodes:
        if(len(D[i])==0):
            return False

    return True



if __name__ == '__main__':
    G,D,C=designConstraintGraph(10)
    print(AC_I(G,D,C))
    print(D)

    # print("->>>>>>>>>>")
    # for i in range(0, 3):
    #
    #     for j in range(i + 1, 3):
    #
    #         for x in D[i]:
    #
    #             for y in D[j]:
    #                 print(x, y, C[(i, j)])
    #                 print(REVISE(x, y, D,C))
