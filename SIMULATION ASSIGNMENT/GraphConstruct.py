import networkx as nx
import random


def manual_data(n):
    m = random.randint(n - 1, n * n)

    domain = {}
    constraint = {}

    fh = open("edgelist.txt", 'r')
    edgeList=fh.readlines()



    # G = nx.read_edgelist(fh)
    G = nx.Graph()



    fh.close()

    G.add_edge(0,1)
    G.add_edge(1,2)
    G.add_edge(0,2)

    return (G)


def getManualGraph(nodes,edges):
    domain = {}
    constraint = {}

    G = nx.gnm_random_graph(nodes,edges, False)


    return (G)



def Noderandom_data(n):

    m = random.randint(n, n*(n-1))



    G = nx.gnm_random_graph(n, m, False)
    # print(G.nodes)
    # print(G.edges)



    # print(domain)
    #print(constraint)
    return (G)


def Edgerandom_data(edge):


    m=edge
    n = random.randint(edge+1,  2* edge)

    G = nx.gnm_random_graph(n, m, False)
    # print(G.nodes)
    # print(G.edges)

    # print(domain)
    # print(constraint)
    return (G)


def Densityrandom_date(density):

    density=density/100
    nodes=random.randint(3,200)
    edges= (density*nodes*(nodes-1))//2

    print(density,"nodes",nodes,"edges", edges)


    G = nx.gnm_random_graph(nodes, edges, False)

    return (G)




def designConstraintGraph(n,par):


    # return manual_data(n)
    if par==1:
        return Noderandom_data(n)
    elif par==2:
        print("Edging")
        return Edgerandom_data(n)
    elif par==3:
        print("density")
        return Densityrandom_date(n)
    # elif par==4:
    #     print("Manual grpah")
    #     return getManualGraph()
