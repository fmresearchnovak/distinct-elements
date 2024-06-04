import math
import random


# approximates the number of distinct elements in the stream A
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
            
        # X will not grow larger than the threshold
        if len(X) == thresh:
            X = filter_half_randomly(X)
            p = p/2
            if len(X) == thresh:
                return len(X)

    return len(X) / p

        
def filter_half_randomly(S): # s is a for "set" !
    for elem in S:
        if(random.random() >= 0.5):
            S.remove(elem)
    return S
    


def main():

    # build up a "stream" of random values.  Of course it's not really a stream, but a list.
    A = []
    while(len(A) != 200):
        A.append(random.randint(0, 5))

    estimated_size = Fsub0(A, 0.98, 0.98)
    print("A: "  + str(A))
    print("Estimated number of distinct (unique) elements in A: " + str(estimated_size))
    

main()
