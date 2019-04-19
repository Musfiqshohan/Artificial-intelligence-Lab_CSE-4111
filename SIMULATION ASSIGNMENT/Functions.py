
def curLabelSize(future):

    potential=0
    for record in future:
        potential+= min(len(record[0]), len(record[1]))

    return potential

def SelectLabelClass(future):

    minVal=1000000000
    minrec=None

    for rec in future:
        val=max(len(rec[0]), len(rec[1]))
        if(val<minVal):
            minVal=val
            minrec=rec


    return minrec[0], minrec[1]

    # return future[0][0],future[0][1]

def SelectVertex(G,graph1):

    maxVal=-1
    maxNd=None
    for nd in G:
        if(graph1.degree(nd)>maxVal):
            maxVal=graph1.degree(nd)
            maxNd=nd

    return maxNd

    # return G[0]


def intersection(A,B):
    return list(set(A) & set(B))


def getNeighbour(graph,v):
    return graph.neighbors(v)

def exclude(A,x):
    Ax= copy.deepcopy(A)
    if(x in Ax):
        Ax.remove(x)
    return Ax


def union(A,x):
    Ax= copy.deepcopy(A)
    Ax.append(x)
    return Ax


def notNeighbour(graph,v):

    nodes=list(graph.nodes)
    neighbours=list(graph.neighbors(v))

    for neg in neighbours:
        if neg in nodes:
            nodes.remove(neg)


    return nodes

