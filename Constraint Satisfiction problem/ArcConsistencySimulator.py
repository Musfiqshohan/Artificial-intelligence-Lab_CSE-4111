import networkx as nx
import random
import copy
from AC_1 import AC_I
from AC_2 import AC_II
from AC_3 import AC_III
from AC_4 import AC_IV
from AC_REVISE import REVISE
from Constraints import isSatisfied
from GraphConstruct import designConstraintGraph, getManualGraph
import matplotlib.pyplot as plt
import time



def getRedution(G,D,Dx):

    totdif=0
    for nodes in G.nodes:
        totdif+=  (len(D[nodes])-len(Dx[nodes]))

    return totdif

def runAC(AC_V,G,D,C, Ycase):
    Gx = copy.deepcopy(G)
    Dx = copy.deepcopy(D)
    Cx = copy.deepcopy(C)
    start = time.time()


    print("AC",AC_V)


    isF=False
    cntchk=0
    if(AC_V==1):
        cntchk = AC_I(Gx, Dx, Cx)
    elif (AC_V == 2):
        cntchk = AC_II(Gx, Dx, Cx)
    elif (AC_V == 3):
        isF,cntchk = AC_III(Gx, Dx, Cx)
    elif (AC_V == 4):
        isF,cntchk = AC_IV(Gx, Dx, Cx)




    end = time.time()
    D1 = copy.deepcopy(Dx)
    # print(end - start)

    required=0
    if Ycase==1:
        required=end - start
    elif Ycase==2:
        required=cntchk
    elif Ycase==3:
        required=getRedution(G,D,Dx)



    print(D1)
    # print(required)


    return D1,required



def getValidSolution(nodes,Xcase):

    while(True):
        G, D, C = designConstraintGraph(nodes,Xcase)
        Gx=copy.deepcopy(G)
        Dx=copy.deepcopy(D)
        Cx=copy.deepcopy(C)
        d,e=AC_I(Gx, Dx, Cx)
        if(d==True):
            break

    return G,D,C



def writeFile(name, data):

    f=open(name+".txt","w")

    res=""

    for d in data:
        d=str(d)
        res=res+d+"\n"
        f.write(res)



def drawGraph(Xaxis, Yaxis,Xcase,Ycase):
    plt.suptitle("Performance analysis of Arc consistency Algorithms")
    plt.title("Md. Musfiqur Rahman , Roll: 05")



    plt.plot(Xaxis, Yaxis[1], label="AC-1")
    plt.plot(Xaxis, Yaxis[2], label="AC-2")
    plt.plot(Xaxis, Yaxis[3], label="AC-3")
    plt.plot(Xaxis, Yaxis[4], label="AC-4")

    writeFile("ac1",Yaxis[1])
    writeFile("ac2",Yaxis[2])
    writeFile("ac3",Yaxis[3])
    writeFile("ac4",Yaxis[4])

    print("Domain:", Xaxis)
    print("ac1",Yaxis[1])
    print("ac2",Yaxis[2])
    print("ac3",Yaxis[3])
    print("ac4",Yaxis[4])

    xlabel=""
    if Xcase==1:
        xlabel="Number of nodes"
    elif Xcase==2:
        xlabel="Number of edges"
    elif Xcase==3:
        xlabel="Graph density"

    if Ycase==1:
        ylabel='execution time'
    elif Ycase==2:
        ylabel='number of constraint checks'
    elif Ycase==3:
        ylabel='Domain reduction'

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.legend(loc='upper left')

    plt.show()




def runExecution(Xcase,Ycase):
    start = 0
    end = 0

    Xaxis = []

    Yaxis = {}
    Yaxis[1] = []
    Yaxis[2] = []
    Yaxis[3] = []
    Yaxis[4] = []

    solutionFound = 0
    r1=3
    r2=200
    inc=10
    if Xcase==1:        #nodes
        r1 = 3
        r2 = 200
        inc=10
    elif Xcase==2:  #edges
        r1= 3
        r2= 100
        inc=10
    elif Xcase==3:  #density
        r1=48
        r2=3
        inc=-5
    # elif Xcase==4:
    #     r1=10
    #     r2=15
    #     inc=10





    for nodes in range(r1, r2, inc):

        print("edges-------------->>>", nodes)

        T1 = 0
        T2 = 0
        T3 = 0
        T4 = 0
        for turn in range(0, 10):   #change here pls !!!!!!!!!!!!!!

            # G, D, C = designConstraintGraph(nodes,1)  # nodes vs
            G, D, C = designConstraintGraph(nodes, Xcase)  # edge vs
            # G,D,C= getValidSolution(nodes,Xcase)
            # G, D, C = getManualGraph(185,510)

            # print("turn-------->")

            t1,t2,t3,t4=0,0,0,0
            D1, t1 = runAC(1, G, D, C,Ycase)
            D2, t2 = runAC(2, G, D, C,Ycase)
            D3, t3 = runAC(3, G, D, C,Ycase)
            D4, t4 = runAC(4, G, D, C,Ycase)

            T1 = (T1 * turn + t1) / (turn + 1.0)
            T2 = (T2 * turn + t2) / (turn + 1.0)
            T3 = (T3 * turn + t3) / (turn + 1.0)
            T4 = (T4 * turn + t4) / (turn + 1.0)

            if (D1 == D2 and D2 == D3 and D3 == D4):
                print("Solution Found")

        if Xcase==3:
            Xaxis.append(nodes/100.0)
        else:
            Xaxis.append(nodes)

        print("======",T1,T2,T3,T4)

        Yaxis[1].append(T1)
        Yaxis[2].append(T2)
        Yaxis[3].append(T3)
        Yaxis[4].append(T4)


    # print(Yaxis[1])
    drawGraph(Xaxis, Yaxis,Xcase,Ycase)



if __name__ == '__main__':


    #for node vs time
    runExecution(1,1)

    #for edge vs time
    # runExecution(2,1)

    #for graph density vs time
    # runExecution(3,1)

    #for node vs constraint satisfaction
    # runExecution(1,2)

    #for edge vs constraint satisfaction
    # runExecution(2,2)

    #for graph density vs constraint satisfaction - number of edges increases but nodes remain little number.For that reason most of the domains
    #  get reduced and number of satisfaction get less.
    # runExecution(3,2)

#     for reduction same to check if all algorithms are okay.
#     runExecution(1,3)



