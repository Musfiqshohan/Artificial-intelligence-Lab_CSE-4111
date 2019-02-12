# https://www.cs.ubc.ca/~mack/Publications/AI77.pdf
import networkx as nx
import random

from AC_REVISE import REVISE
from Constraints import isSatisfied
from GraphConstruct import designConstraintGraph


def AC_II(G,D, C):

    n= G.number_of_nodes()
    for i in range(0,n):


        queue1=[]
        for e in G.edges:
            x,y=e
            x,y= max(x,y), min(x,y)
            queue1.append((x,y))

        queue2=[]
        for e in G.edges:
            x, y = e
            x,y= min(x,y), max(x,y)
            queue2.append((x,y))



        while(len(queue1)!=0):

            while(len(queue1)!=0):


                edge= queue1.pop(0)
                k,m=edge

                if(REVISE(k,m,D,C)):

                    for e in G.edges:
                        x,y=e
                        if(x==k and y<=i  and y!=m):
                            queue2.append((y,x))
                        elif(y==k and x<=i and x!=m):
                            queue2.append((x,y))

                if(len(D[k])==0):
                    return False

            queue1=queue2
            queue2=[]



    for i in G.nodes:
        if(len(D[i])==0):
            return False

    return True








if __name__ == '__main__':
    G,D,C=designConstraintGraph(10)
    print(AC_II(G,D,C))
    print(D)
