from GraphConstruct import designConstraintGraph
import copy
import networkx as nx
import time
import matplotlib.pyplot as plt
import random

incumbent=[]
# class Label():
#     G = []
#     H = []
#
#     def __init__(self,Gx,Hx):
#
#         self.G=copy.deepcopy(Gx)
#         self.H=copy.deepcopy(Hx)



graph1=nx.Graph()
graph2=nx.Graph()






def search(future, M):

    global incumbent
    if(len(M)> len(incumbent)):
        incumbent=copy.deepcopy(M)
    bound= len(M) + curLabelSize(future)

    if(bound<= len(incumbent)):
        return

    global graph1, graph2
    G,H= SelectLabelClass(future)

    v=SelectVertex(G,graph1)



    for w in H:
        newFuture = []

        for record in future:
            newG=record[0]
            newH=record[1]


            newnewG=exclude(intersection(newG, getNeighbour(graph1,v)) , v)
            newnewH=exclude(intersection(newH, getNeighbour(graph2,w)) , w)

            if(len(newnewG)!=0 and len(newnewH)!=0):
                newFuture=union(newFuture,(newnewG,newnewH))
                # newFuture.append(Label())

            newnewG= exclude(intersection(newG, notNeighbour(graph1,v)) , v)
            newnewH= exclude(intersection(newH, notNeighbour(graph2,w)) , w)

            if (len(newnewG) != 0 and len(newnewH) != 0):
                newFuture = union(newFuture, (newnewG, newnewH))
                # newFuture.append(Label(newnewG, newnewH))

        newM=copy.deepcopy(M)
        newM.append((v,w))
        search(newFuture,newM)

    newG= exclude(G,v)
    future=exclude(future,(G,H))
    if(len(newG)!=0):
        future= union(future,(newG,H))

    search(future,M)






def McSplit(G,H):



    global incumbent

    incumbent=[]
    future=[]
    M=[]

    #G,H list of nodes maybe

    future.append((G,H))

    # print(future[0][0][0])

    search(future, M)

    return incumbent


def check_solution(ret):
    res1 = []
    res2 = []
    for tup in ret:
        res1.append(tup[0])
        res2.append(tup[1])

    xx = graph1.subgraph(res1)
    # print(xx.edges)

    yy = graph2.subgraph(res2)
    # print(yy.edges)

    print(nx.is_isomorphic(xx, yy))


def drawGraph(Xaxis, Yaxis):
    plt.suptitle("(a) Unlabelled, undirected, not connected")
    plt.title("Md. Musfiqur Rahman , Roll: 05")



    plt.plot(Xaxis, Yaxis, label="MCSPLIT")


    plt.xlabel("Number of nodes")
    plt.ylabel("Runtime (ms)")

    plt.legend(loc='upper left')

    plt.show()



def getGraph():

    edges1 = random.randint(nodeNo, nodeNo + 10)
    graph1 = nx.gnm_random_graph(nodeNo, edges1, False)

    edges2 = random.randint(nodeNo, nodeNo + 10)
    graph2 = nx.gnm_random_graph(nodeNo, edges2, False)

    return graph1,graph2


def getManual_graph():

    graph1 = nx.Graph()
    graph2 = nx.Graph()

    graph1.add_edge(1,2)
    graph1.add_edge(3,4)

    graph2.add_edge(1,2)
    graph2.add_edge(3,4)

    return graph1, graph2


def getExecutedTime(nodeNo):
    start = time.time()

    global graph1, graph2

    # graph1,graph2=getGraph()
    graph1,graph2=getManual_graph()


    G = list(graph1.nodes)
    H = list(graph2.nodes)

    ret = McSplit(G, H)
    print("answer:",ret)

    end = time.time()

    executeTime = end - start

    return executeTime

if __name__ == '__main__':



    # graph1=designConstraintGraph(30,1)

    Xaxis=[]
    Yaxis=[]
    for nodeNo in range(3,4):

        sum=0
        for iter in range(0,3):
            sum+=getExecutedTime(nodeNo)

        avg=sum/3

        print(nodeNo, "->", avg)

        Xaxis.append(nodeNo)
        Yaxis.append(avg*1000)
        # check_solution(ret)


    drawGraph(Xaxis,Yaxis)


