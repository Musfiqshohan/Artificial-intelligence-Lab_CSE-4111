from queue import Queue


def isSatisfied(X,Y, id):

    if(id==0):
        return X<Y
    if(id==1):
        return X<=3*Y
    if(id==2):
        return X==Y



domain=[]
const={}
def graph_input():

    n=3

    adj=[]
    global domain
    for i in range(0,n):
        x=[]
        adj.append(x)
        domain.append(x)
        const.append(x)

    adj[0]=[0,1]
    adj[1]=[0,2]
    adj[2]=[1,2]


    const[(0,1)]=0
    const[(0,2)]=1
    const[(1,2)]=2



    domain[0]=[1,2,3]
    domain[1]=[2,4,5]
    domain[2]=[2,5,6]








    # for i in range(0,n):
    #     u=int(input())
    #     v=int(input())
    #     print(u,v)
    #     adj[u].append(v)
    #     adj[v].append(u)


    return  (n,adj)


def AC_3():

    (n,adj)=graph_input()

    queue=[]
    for i in range(0, n):
        for j in range(0, len(adj[i])):
            queue.append((i,adj[i][j]))


    print(queue)


    # while(len(queue)!=0):
    #     xi,xj= queue.pop(0)
    #
    #     if(REVISE(xi,xj)):
    #         if()




def REVISE(xi,xj):
    revised=False
    global domain,const
    for x in range(len(domain[xi])):
        flag=0
        for y in range(len(domain[xj])):
            if(isSatisfied(xi,xj,const[(xi,xj)])==True):
                flag=1
                break

        if(flag==0):
            domain.len()








if __name__ == '__main__':
    AC_3()