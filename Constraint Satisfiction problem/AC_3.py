import networkx as nx
import random

from AC_REVISE import REVISE
from Constraints import isSatisfied
from GraphConstruct import designConstraintGraph


def AC_III(G,D, C):

    queue=[]

    for e in G.edges:
        queue.append(e)

    while(len(queue)!=0):
        #print("Q=",queue)

        edge= queue.pop(0)
        Xi,Xj=edge

        if(REVISE(Xi,Xj,D,C)):
            if(len(D)==0):
                return False

            for Xk in  G.neighbors(Xi):
                if(Xk==Xj):
                    continue
                else:
                    queue.append((Xk,Xi))

    return True




if __name__ == '__main__':
    G,D,C=designConstraintGraph(10)
    #print(AC_III(G,D,C))
    #print(D)


    # #print("->>>>>>>>>>")
    # for i in range(0, 3):
    #
    #     for j in range(i+1, 3):
    #
    #         for x in D[i]:
    #
    #             for y in D[j]:
    #
    #                 #print(x,y,C[(i,j)])
    #                 #print(isSatisfied(x,y,C[(i,j)]))







