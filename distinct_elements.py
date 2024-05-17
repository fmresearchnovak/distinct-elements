import math
import random

def Fsub0(A, ep, d):
    p = 1
    X = set()
    m = len(A) - 1
    thresh = 12/ep**2 * math.log(8*m / d)
    print(thresh)

    for a_i in A:
        
        # discard() does not throw an exception when A[i] is not present
        X.discard(a_i) # X <- X \ {a_i}
        if(random.random() < p): # with probability p
            X.add(a_i) # X <- X U {a_i}
            
        if len(X) == thresh:
            X = throw_away(X)
            p = p/2
            if len(X) == thresh:
                return len(X)

    return len(X) / p

        
def throw_away(S): # s is a for "set" ! :D
    for elem in S:
        if(random.random() >= 0.5):
            S.remove(elem)
    return S
    


def main():

    # build up a set of random values
    A = []
    while(len(A) != 200):
        A.append(random.randint(0, 5))

    estimated_size = Fsub0(A, 0.98, 0.98)
    print("A: "  + str(A))
    print("Estimated size of A: " + str(estimated_size))
    

main()
