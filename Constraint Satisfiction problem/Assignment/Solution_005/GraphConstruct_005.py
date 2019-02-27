import networkx as nx
import random


def manual_data(n):
    m = random.randint(n - 1, n * n)

    domain = {}
    constraint = {}

    fh = open("edgelist.txt", 'r')
    edgeList=fh.readlines()
    fd = open('domain.txt', "r")
    domList = fd.readlines()
    fc = open('constraint.txt', "r")
    consList = fc.readlines()


    # G = nx.read_edgelist(fh)
    G = nx.Graph()



    fh.close()
    fc.close()
    fd.close()


    # for ln in  edgeList:
    #
    #     ln = ln.strip().split(" ")
    #     ln2 = []
    #     for x in ln:
    #         ln2.append(int(x))
    #     G.add_edge(ln[0],ln[1])

    G.add_edge(0,1)
    G.add_edge(1,2)
    G.add_edge(0,2)



    # domain[0]=[2,5,9,11,5,6]
    # domain[1]=[2,5,10,2,5,6,7]
    # domain[2]=[2,6,5,11,21,5,6,6,7]
    domain[0]=[11]
    domain[1]=[5]
    domain[2]=[11,21]

    constraint[(0,1)]=0
    constraint[(1,2)]=2
    constraint[(0,2)]=3



    return (G, domain, constraint)


def getManualGraph(nodes,edges):
    domain = {}
    constraint = {}

    G = nx.gnm_random_graph(nodes,edges, False)

    for nd in G.nodes:
        domain[nd] = random.sample(range(1, 1000), 50)

    numberOfConst = 6
    for e in G.edges:
        constraint[e] = random.randint(0, numberOfConst)

    return (G, domain, constraint)



def Noderandom_data(n):

    m = random.randint(n, n*(n-1))

    domain = {}
    constraint = {}

    G = nx.gnm_random_graph(n, m, False)
    # print(G.nodes)
    # print(G.edges)


    for nd in G.nodes:
        # domain[nd]=random.sample(range(1, 100), 10)
        domain[nd]=random.sample(range(1, 1000), 10)

    numberOfConst = 6
    for e in G.edges:
        constraint[e] = random.randint(0, numberOfConst)

    # print(domain)
    #print(constraint)
    return (G, domain, constraint)


def Edgerandom_data(edge):


    m=edge
    n = random.randint(edge+1,  2* edge)
    domain = {}
    constraint = {}

    G = nx.gnm_random_graph(n, m, False)
    # print(G.nodes)
    # print(G.edges)

    for nd in G.nodes:
        # domain[nd]=random.sample(range(1, 100), 10)
        domain[nd] = random.sample(range(1, 1000), 50)

    numberOfConst = 6
    for e in G.edges:
        constraint[e] = random.randint(0, numberOfConst)

    # print(domain)
    # print(constraint)
    return (G, domain, constraint)


def Densityrandom_date(density):

    density=density/100
    nodes=random.randint(3,200)
    edges= (density*nodes*(nodes-1))//2

    print(density,"nodes",nodes,"edges", edges)

    domain = {}
    constraint = {}

    G = nx.gnm_random_graph(nodes, edges, False)
    # print(G.nodes)
    # print(G.edges)

    for nd in G.nodes:
        # domain[nd]=random.sample(range(1, 100), 10)
        domain[nd] = random.sample(range(1, 1000), 50)

    numberOfConst = 6
    for e in G.edges:
        constraint[e] = random.randint(0, numberOfConst)

    # print(domain)
    # print(constraint)
    return (G, domain, constraint)




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







designConstraintGraph(10,1)