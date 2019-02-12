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



    domain[0]=[1,2 ,3,9,2,5,88]
    domain[1]=[1,2 ,4,10,6,7,123,22,5,6]
    domain[2]=[1,2 ,5,2,4,5]

    constraint[(0,1)]=0
    constraint[(1,2)]=2
    constraint[(0,2)]=3


    # for nd,ln in zip(G.nodes,domList):
    #
    #     ln=ln.strip().split(" ")
    #     ln2=[]
    #     for x in ln:
    #         ln2.append(int(x))
    #     domain[nd]=ln2



    # for e,ln in zip(G.edges,consList):
    #     # constraint[e] = random.randint(0, numberOfConst)
    #     ln = ln.strip().split(" ")
    #     for x in ln:
    #         constraint[e]=int(x)



    #print(G.nodes)
    #print(G.edges)
    #print(domain)
    #print(constraint)
    return (G, domain, constraint)


def random_data(n):

    m = random.randint(n, n*(n-1))

    domain = {}
    constraint = {}

    G = nx.gnm_random_graph(n, m, False)
    # print(G.nodes)
    # print(G.edges)


    for nd in G.nodes:
        # domain[nd]=random.sample(range(1, 100), 10)
        domain[nd]=random.sample(range(1, 100), 50)

    numberOfConst = 6
    for e in G.edges:
        constraint[e] = random.randint(0, numberOfConst)

    # print(domain)
    #print(constraint)
    return (G, domain, constraint)


def designConstraintGraph(n):


    # return manual_data(n)
    return random_data(n)






designConstraintGraph(10)