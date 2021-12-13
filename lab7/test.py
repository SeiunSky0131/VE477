import random
import time
import numpy as np

def RandomSearch(A, size, k):
    k: int # target number
    index: int
    index_visited: list

    index_visited = [1 for i in range(0, size)]

    while sum(index_visited)!= 0:
        index = random.randint(0, size - 1) # generate a new random index

        # we will first check whether the index is what we want
        if A[index] == k:
            return index

        # if index is not what we want and have not been visited, add to the visited list
        index_visited[index] = 0
    
    return -1 # -1 represents there is no such matching

def LinearSearch(A, size, k):
    for i in range (0,size):
        if A[i] == k:
            return i
    return -1 # -1 for no such matching

def ScrambleSearch(A, size, k):
    random.shuffle(A)
    return LinearSearch(A,size,k)


if __name__ == "__main__":
    number_range = 10000 # you will never want to try 1 million! Or you may want to use multi-threading
    times = 30 # repeat for 30 times to get the average value

    t_random = []
    t_linear = []
    t_scramble = []

    for t in range(0, times):
        print("Begin the ", t, "time test")
        A = [random.randint(1, number_range) for i in range(number_range)]
        k = random.randint(1, number_range)

        start_time = time.time()
        print ("Random Search result is: ", RandomSearch(A, number_range, k), " Random Search time is ", time.time() - start_time)
        t_random.append(time.time()-start_time)

        start_time = time.time()
        print ("Linear Search result is: ", LinearSearch(A, number_range, k), " Linear Search time is ", time.time() - start_time)
        t_linear.append(time.time()-start_time)

        start_time = time.time()
        print ("Scramble Search result is: ", ScrambleSearch(A, number_range, k), " Scramble Search time is ", time.time() - start_time)
        t_scramble.append(time.time()-start_time)        

    print("Random search average time is: ", np.average(t_random))
    print("Linear search average time is: ", np.average(t_linear))
    print("Scramble search average time is: ", np.average(t_scramble))