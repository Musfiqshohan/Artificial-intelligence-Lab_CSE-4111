import copy

from Constraints import isSatisfied


def REVISE(Xi,Xj,D,C):
    revised=False

    #print("Xi->Xj",Xi,Xj)
    #print("Before->",D[Xi])
    # List1=list.copy(D[Xi])
    # List2=list.copy(D[Xj])
    List1=copy.deepcopy(D[Xi])
    List2=copy.deepcopy(D[Xj])

    cntcheck=0

    for x in List1:

        flag=False
        for y in List2:


            if((Xi,Xj) not in C):
                x,y=y,x
                cid=C[(Xj,Xi)]
            else:
                cid=C[(Xi,Xj)]


            if(isSatisfied(x,y,cid)):
                cntcheck+=1
                #print("Satisfied:",x,y,cid)
                flag=True
            # else:
                #print("Not Satisfied:", x, y, cid)

            if ((Xi, Xj) not in C):
                x, y = y, x



        if(flag==False):
            #print("Eliminating :",x)
            D[Xi].remove(x)
            revised=True

    # if(revised):
        #print("After->",D[Xi])
    return revised,cntcheck