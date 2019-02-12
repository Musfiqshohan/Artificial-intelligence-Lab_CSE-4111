import networkx as nx
import random

from AC_1 import AC_I
from AC_2 import AC_II
from AC_3 import AC_III
from AC_4 import AC_IV
from AC_REVISE import REVISE
from Constraints import isSatisfied
from GraphConstruct import designConstraintGraph
import matplotlib.pyplot as plt
import time






if __name__ == '__main__':


    perf1=[]
    perf2=[]
    perf3=[]

    start = 0
    end = 0

    Xaxis=[]

    Yaxis={}
    Yaxis[AC_I]=[]
    Yaxis[AC_II]=[]
    Yaxis[AC_III]=[]
    Yaxis[AC_IV]=[]

    solutionFound=0
    r1=3
    r2=20
    for nodes in range(r1,r2,1):

        G, D, C = designConstraintGraph(nodes)
        # while(True):
        #     G, D, C = designConstraintGraph(nodes)
        #     Gx=G.copy()
        #     Dx=D.copy()
        #     Cx=C.copy()
        #
        #     if(AC_I(Gx, Dx, Cx)==True):
        #         break

        ####### AC-1 ###########
        Gx = G.copy()
        Dx = D.copy()
        Cx = C.copy()
        start = time.time()
        AC_I(Gx, Dx, Cx)
        end = time.time()
        D1=Dx.copy()
        print(end - start)
        Yaxis[AC_I].append(end - start)



        ##########AC-2###########
        Gx = G.copy()
        Dx = D.copy()
        Cx = C.copy()
        start = time.time()
        AC_II(Gx, Dx, Cx)
        end = time.time()
        D2=Dx.copy()
        print(end - start)
        Yaxis[AC_II].append(end - start)

        ##########AC-3###########
        Gx = G.copy()
        Dx = D.copy()
        Cx = C.copy()
        start = time.time()
        AC_III(Gx, Dx, Cx)
        end = time.time()
        D3=Dx.copy()
        print(end - start)
        Yaxis[AC_III].append(end - start)

        ##########AC-4###########
        Gx = G.copy()
        Dx = D.copy()
        Cx = C.copy()
        start = time.time()
        AC_IV(Gx, Dx, Cx)
        end = time.time()
        D4 = Dx.copy()
        print(end - start)
        Yaxis[AC_IV].append(end - start)

        print(D1)
        print(D2)
        print(D3)
        print(D4)
        # if (len(D1) != 0 and len(D2)!=0 and len(D3)!=0 and len(D4)!=0):
        #     solutionFound += 1



    print("->",solutionFound,"/",(r2-r1+1))

    #     Xaxis.append(nodes)
    #
    #
    # print(Yaxis[AC_I])
    # print(Yaxis[AC_II])
    # print(Yaxis[AC_III])
    # print(Yaxis[AC_IV])
    #
    # plt.plot(Xaxis, Yaxis[AC_I],label = "AC-1")
    # plt.plot(Xaxis, Yaxis[AC_II],label = "AC-2")
    # plt.plot(Xaxis, Yaxis[AC_III],label = "AC-3")
    # plt.plot(Xaxis, Yaxis[AC_IV],label = "AC-4")
    #
    # plt.xlabel('x - axis')
    # # naming the y axis
    # plt.ylabel('y - axis')
    #
    # plt.legend(loc='upper left')
    #
    # # function to show the plot
    # plt.show()
