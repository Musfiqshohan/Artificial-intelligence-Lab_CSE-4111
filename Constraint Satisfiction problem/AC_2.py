# https://www.cs.ubc.ca/~mack/Publications/AI77.pdf
import networkx as nx
import random

from AC_REVISE import REVISE
from Constraints import isSatisfied
from GraphConstruct import designConstraintGraph


def AC_II(G,D, C):

    cnstcheck = 0
    n= G.number_of_nodes()
    for i in range(0,n+1):


        queue1=[]
        queue2=[]

        # print(G.edges)
        for e in G.edges:
            x,y=e
            # x,y= max(x,y), min(x,y)

            # if(y<x):

            if(y==i):
                x,y=y,x

            if(x==i and y<i):
                queue1.append((x, y))
                queue2.append((y, x))




            # x,y=y,x
            #
            # if (y < x):
            #     queue1.append((x, y))
            #     queue2.append((y, x))








        while(len(queue1)!=0):

            while(len(queue1)!=0):

                edge= queue1.pop(0)
                k,m=edge

                d,cntch=REVISE(k,m,D,C)
                cnstcheck+=cntch
                if(d):


                    neighbours=G.neighbors(k)

                    for p in neighbours:

                        if(p<=i and p!=m):
                            queue2.append((p,k))

                        # print(e)
                        # x,y=e
                        # if(x==k and y<=i  and y!=m):
                        #     queue2.append((y,x))
                        # elif(y==k and x<=i and x!=m):
                        #     queue2.append((x,y))

            queue1=queue2
            queue2=[]




    return cnstcheck




if __name__ == '__main__':
    G,D,C=designConstraintGraph(10)
    AC_II(G,D,C)
    print(D)
