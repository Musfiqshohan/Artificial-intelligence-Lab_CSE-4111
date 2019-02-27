# https://www.cs.ubc.ca/~mack/Publications/AI77.pdf
import networkx as nx
import random

from AC_REVISE import REVISE
from Constraints import isSatisfied
from GraphConstruct import designConstraintGraph


def AC_I(G,D, C):

    queue=[]

    cnstcheck=0

    for e in G.edges:
        x,y=e
        e1=x,y
        e2=y,x
        queue.append(e1)
        queue.append(e2)


    while(True):
        change = False

        for edge in queue:
            Xi,Xj=edge
            d,cntch=REVISE(Xi,Xj,D,C)
            cnstcheck+=cntch
            change=change or d

            # if(d):
            #     if(len(D[Xi])==0 or len(D[Xj])==0):
            #         return False


        if(change==False):
            break
        else:
            continue

    return cnstcheck


if __name__ == '__main__':
    G,D,C=designConstraintGraph(10)
    AC_I(G,D,C)
    print(D)
