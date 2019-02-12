from math import gcd


def isSatisfied(X, Y, id):
    if (id == 0):
        #print("abs(X-Y):" ,abs(X-Y), " > gcd(X,Y):",gcd(X,Y) )
        # return abs(X-Y)> gcd(X,Y)
        if(abs(X-Y)> gcd(X,Y)):
            return True
        else:
            return False

    if (id == 1):
        #print("Y:",Y,"==X*X:",X*X)
        # return Y==X*X
        if(Y==X*X):
            return True
        else:
            return False


    if (id == 2):
        #print("X*X:",X*X,"+Y*Y:",Y*Y,">100")
        # return X*X + Y*Y>10*10
        if(X*X + Y*Y>10*10):
            return True
        else:
            return False

    if (id ==3):
        #print("Y:",Y,"==X:",X)
        # return Y==X
        if(Y==X):
            return True
        else:
            return False


    if(id==4):
        #print("X*X:",X*X,"-4*1*Y:",-4*1*Y,">0")
        # return X*X-4*1*Y>=0
        if(X*X-4*1*Y>=0):
            return True
        else:
            return False

    if(id==5):
        #print("X:",X,"Y:",Y,"X^Y:",(X^Y)%2)
        # return (X^Y)%2
        if((X^Y)%2==1):
            return True
        else:
            return False



