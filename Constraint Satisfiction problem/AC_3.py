import networkx as nx
import random

from AC_REVISE import REVISE
from Constraints import isSatisfied
from GraphConstruct import designConstraintGraph


def AC_III(G,D, C):

    queue=[]
    cnstcheck=0

    for e in G.edges:
        x,y=e
        queue.append((x,y))
        queue.append((y,x))

    while(len(queue)!=0):

        edge= queue.pop(0)
        Xk,Xm=edge

        d,cntch=REVISE(Xk,Xm,D,C)
        cnstcheck+=cntch
        # print("AC3->", cnstcheck)
        if(d):

            if(len(D[Xk])==0):
                return False,cnstcheck

            for Xi in  G.neighbors(Xk):
                if(Xi==Xk or Xi==Xm):
                    continue
                else:
                    queue.append((Xi,Xk))

    return True,cnstcheck

if __name__ == '__main__':
    G,D,C=designConstraintGraph(10)
    print(AC_III(G,D,C))
    print(D)


