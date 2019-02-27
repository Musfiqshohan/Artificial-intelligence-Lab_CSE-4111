# https://www.cs.ubc.ca/~mack/Publications/AI77.pdf
import copy
import networkx as nx
import random

from AC_REVISE import REVISE
from Constraints import isSatisfied
from GraphConstruct import designConstraintGraph


def AC_IV(G,D, C):

    queue=[]
    S={}
    counter={}

    cnstcheck=0

    for vi in G.nodes:
        for ai in D[vi]:
            for vj in G.nodes:
                counter[(vi,ai,vj)]=0

    for vj in G.nodes:
        for aj in D[vj]:
            S[(vj,aj)]=[]


    edgeList=[]
    for edge in G.edges:
        x,y=edge
        edgeList.append((x,y))
        edgeList.append((y,x))


    # print(edgeList)

    cnt=0
    for edge in edgeList:
        vi,vj=edge


        # dom1=list.copy(D[vi])
        # dom2=list.copy(D[vj])
        dom1=copy.deepcopy(D[vi])
        dom2=copy.deepcopy(D[vj])

        # print(vi,vj)

        cnt+=1
        # print("edge count->",cnt, "dom size:", len(dom1), len(dom2))

        for ai in dom1:
            for aj in dom2:


                if ((vi, vj) not in C):
                    axi, axj = aj, ai
                    cid = C[(vj, vi)]           #here maybe problem
                else:
                    axi, axj=ai,aj
                    cid = C[(vi, vj)]

                if (isSatisfied(axi, axj, cid)):
                    cnstcheck+=1
                    counter[(vi,ai,vj)]=counter[(vi,ai,vj)]+1
                    S[(vj,aj)].append((vi,ai))




            if(counter[(vi,ai,vj)]==0):
                queue.append((vi,ai))
                D[vi].remove(ai)

                # if(len(D[vi])==0):
                #     return False,cnstcheck

        # print("AC4 satisfy->",cnstcheck)

    while(len(queue)!=0):
        vj,aj=queue.pop(0)

        for edge in S[(vj,aj)]:
            vi,ai=edge

            dom=copy.deepcopy(D[vi])
            if(ai in dom):
                counter[(vi,ai,vj)]=counter[(vi,ai,vj)]-1
                if(counter[(vi,ai,vj)]==0):
                    queue.append((vi,ai))
                    D[vi].remove(ai)

                    # if (len(D[vi]) == 0):
                    #     return False,cnstcheck


    return True,cnstcheck



if __name__ == '__main__':
    G,D,C=designConstraintGraph(10)
    AC_IV(G,D,C)
    print(D)

