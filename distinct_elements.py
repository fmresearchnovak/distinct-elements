import math
import random



class Fsub0:
    def __init__(self, ep, d):
        self._ep = ep
        self._d = d
        self._p = 1
        self._X = set()
        self._thresh = 12/ep**2 * math.log(8 / d)
        self._room_for_more = True


    def process_stream_element(self, a_i):

        if(not self._room_for_more):
            return len(self._X) 
        
        # discard() does not throw an exception when A[i] is not present
        self._X.discard(a_i) # X <- X \ {a_i}
        if(random.random() < self._p): # with probability p
            self._X.add(a_i) # X <- X U {a_i}
            
        # X will not grow larger than the threshold
        if len(self._X) == self._thresh:
            self._X = filter_half_randomly(self._X)
            self._p = self._p/2
            if len(self._X) == self._thresh:
                self._room_for_more = False
        
        # return the current estimate
        return len(self._X) / self._p


    def get_estimate(self):
        return len(self._X) / self._p

'''
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
'''
        
def filter_half_randomly(S): # s is a for "set" !
    for elem in S:
        if(random.random() >= 0.5):
            S.remove(elem)
    return S
    



def debugging_test():
    # build up a "stream" of random values.  Of course it's not really a stream, but a list.
    A = []
    while(len(A) != 200):
        A.append(random.randint(0, 5))
    print("A: "  + str(A))

    Fsub0_instance = Fsub0(0.98, 0.98)
    for a_i in A:
        #print("\tinserting: " + str(a_i))
        estimated_size = Fsub0_instance.process_stream_element(a_i)
        #print("\testimated number of unique elements is: " + str(estimated_size))

    print("Estimated number of distinct (unique) elements in A: " + str(estimated_size))
    assert(estimated_size == 6)
    print("PASSED!")



def dictionary_test():
    fh = open("american-english", "r")
    size = 97239 # num bytes in the file, (according to stat command), 1 byte = 1 character

    Fsub0_instance = Fsub0(0.90, 0.90)

    count = 0
    while(count < 2000):
        # read random letter from the file fh
        i = random.randint(0, size)
        # read the i-ith character (string) from fh
        #print("i: " + str(i))
        fh.seek(i)

        try:
            letter = fh.read(1)
            #print("\t i*2:" + str(i) + "  character: " + str(letter))
            Fsub0_instance.process_stream_element(letter)
            count = count + 1

        except UnicodeDecodeError:
            continue
        


    print("Estimated number of distinct (unique) elements in dictionary file: " + str(Fsub0_instance.get_estimate()))


def main():

    #debugging_test()
    dictionary_test()
    

if __name__ == "__main__":
    main()
