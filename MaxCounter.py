def solution(N, A):
    # write your code in Python 3.6
    ln = N
    ar = [0]*ln
    max_counter = 0
    for c in A:
        #print(max_counter)
        if 1<=c<=ln:
            idx_val = c-1
            ar[idx_val] = ar[idx_val]+1
            max_counter = max(max_counter, ar[idx_val])
        else:
            # pass
            #print("Setting to max"+str(ar))
            ar = [max_counter]*ln
            # counter is max so set all to max value of any counter
        #print(""+str(ar))
    return ar

#print(solution(5 , [3,4,4,6,1,4,4]))
