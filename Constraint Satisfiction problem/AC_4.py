# https://www.cs.ubc.ca/~mack/Publications/AI77.pdf
import networkx as nx
import random

from AC_REVISE import REVISE
from Constraints import isSatisfied
from GraphConstruct import designConstraintGraph


def AC_IV(G,D, C):

    queue=[]
    S={}
    counter={}

    for vi in G.nodes:
        for ai in D[vi]:
            for vj in G.nodes:
                counter[(vi,ai,vj)]=0

    for vj in G.nodes:
        for aj in D[vj]:
            S[(vj,aj)]=[]


    for edge in G.edges:
        vi,vj=edge


        dom1=list.copy(D[vi])
        dom2=list.copy(D[vj])

        for ai in dom1:
            for aj in dom2:
                # if(isSatisfied(ai,aj,C[(ai,aj)]))
                if ((vi, vj) not in C):
                    vi, vj = vj, vi
                    cid = C[(vj, vi)]
                else:
                    cid = C[(vi, vj)]

                if (isSatisfied(ai, aj, cid)):
                    counter[vi,ai,vj]=counter[vi,ai,vj]+1
                    S[(vj,aj)].append((vi,ai))


            if(counter[(vi,ai,vj)]==0):
                queue.append((vi,ai))
                D[vi].remove(ai)

    while(len(queue)!=0):
        vj,aj=queue.pop(0)

        for edge in S[(vj,aj)]:
            vi,ai=edge
            if(ai in D[vi]):
                counter[(vi,ai,vj)]=counter[(vi,ai,vj)]-1
                if(counter[(vi,ai,vj)]==0):
                    queue.append((vi,ai))
                    D[vi].remove(ai)









if __name__ == '__main__':
    G,D,C=designConstraintGraph(10)
    print(AC_IV(G,D,C))
    print(D)

